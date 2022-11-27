# Only update things that have changed if the path resets

#


import pygame
import pygame.locals
from time import time
from multiprocessing import Process
from pprint import pprint
from sys import setrecursionlimit
from copy import deepcopy
import numpy as np
setrecursionlimit(10000)

input_file = 'sample_input'
tick = 0
window_size = (800, 800)
font_type = 'Source Code Pro'
font_size = window_size[0]
tile_size = window_size[0]
use_pygame = True
part_2 = False
if input_file == 'sample_input':
    font_size //= 20
    tile_size //= 10
else:
    font_size //= 200
    tile_size //= 100

if part_2:
    font_size //= 5
    tile_size //= 5
computer_time = 0
real_time = time()


colors = {
    'BLUE': (0, 0, 222),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'GREEN': (0, 200, 0),
    'RED': (220, 0, 0)
}

pygame.init()
display = pygame.display.set_mode(window_size)
pygame.display.set_caption('AOC DAY 15')
fill = pygame.Surface((225, 40))
fill.fill(colors['BLACK'])

font = pygame.font.SysFont(font_type, font_size)
low_risk_font = pygame.font.SysFont(font_type, 50)
time_font = pygame.font.SysFont(font_type, 30)


class Solution:
    def __init__(self, values):
        self.values = [list(map(int, list(x))) for x in values]
        if part_2:
            self.make_large_grid()
        if not isinstance(self.values, np.ndarray):
            self.values = np.asarray(self.values)

        total = 0
        for row in self.values[1:-1]:
            total += row[0]
        total += sum(self.values[-1])

        self.risks = [[total for x in y] for y in self.values]

        self.dirs = [1, 0, -1]
        self.lowest_risk = total

    def make_large_grid(self):
        values = self.values
        grid_row = []
        for row in range(len(values)):
            r = values[row] * 5
            grid_row.append(r)
        self.values = grid_row * 5

        self.values = np.asarray(self.values)

        for r in range(1, 5):
            low = r * self.values.shape[0] // 5
            high = (r+1) * self.values.shape[0] // 5
            self.values[low:][:] += 1
            self.values[low:][:] = np.where(
                self.values[low:][:] > 9, 1, self.values[low:][:])
            self.values[:][low:] += 1
            self.values[:][low:] = np.where(
                self.values[:][low:] > 9, 1, self.values[:][low:])

        print(self.values)

    def get_lowest_risk(self, pos, previous_risk, visited):
        global computer_time
        self.pygame_low_risk()
        t1 = time()
        x, y = pos
        current_risk = previous_risk + self.values[x][y]
        visited[pos] = True
        computer_time += time() - t1
        self.pygame_update_only(pos, visited)
        if self.risks[x][y] <= current_risk:
            return
        if current_risk > self.lowest_risk:
            return
        t1 = time()
        self.risks[x][y] = current_risk
        if x == len(self.values)-1 and y == len(self.values[-1])-1:
            computer_time += time() - t1
            self.pygame_events(visited)
            t1 = time()
            self.lowest_risk = min(self.lowest_risk, current_risk)
            self.risks[x][y] = min(self.risks[x][y], current_risk)
            computer_time += time() - t1
            return

        computer_time += time() - t1
        self.pygame_time_display()
        for i in self.dirs:
            for j in self.dirs:
                if abs(i) == abs(j):
                    continue
                if x+i < 0 or x+i >= len(self.values) or y+j < 0 or y+j >= len(self.values):
                    continue
                if not visited[(x+i, y+j)]:
                    if self.risks[x+i][y+j] < current_risk + self.values[x+i][y+j]:
                        # self.risks[x][y] = self.risks[x+i][y+j] + self.values[x][y]
                        continue
                    # pprint(self.risks)
                    self.get_lowest_risk((x+i, y+j), current_risk, visited)
                    visited[(x+i, y+j)] = False
                    self.pygame_update_only((x+i, y+j), visited)

    def run(self):
        starting_postion = (0, 0)

        visited = {}
        for x in range(len(self.values)):
            for y in range(len(self.values)):
                visited[(x, y)] = False

        self.pygame_events(visited)
        self.get_lowest_risk(starting_postion, 0, visited)

    def pygame_time_display(self):
        if use_pygame:
            global real_time
            text = time_font.render(
                str(round(computer_time/7.2, 10)), True, colors['RED'])
            display.blit(fill, (10, window_size[1]-40))
            display.blit(text, (15, window_size[1]-40))
            text = time_font.render(
                str(round(time()-real_time)), True, colors['RED'])
            display.blit(fill, (window_size[0]-80, window_size[1]-40))
            display.blit(text, (window_size[0]-80, window_size[1]-40))
            pygame.display.update()

    def pygame_low_risk(self):
        if use_pygame:
            text = low_risk_font.render(
                str(self.lowest_risk), True, colors['GREEN'])
            display.blit(text, (0, 0))
            pygame.display.update()

    def pygame_events(self, visited):
        if use_pygame:
            global tick
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    if event.button == 5:  # Wheel Down / Speed up
                        if tick == 0:
                            pass
                        elif tick > 240:
                            tick = 0
                        else:
                            if tick > 30:
                                tick += 5
                            else:
                                tick += 1
                    elif event.button == 4:  # Wheel Up / Slow down
                        if tick == 1:
                            pass
                        elif tick == 0:
                            tick = 240
                        else:
                            if tick > 30:
                                tick -= 5
                            else:
                                tick -= 1
                    pygame.time.Clock().tick(tick)

            fill = pygame.Surface(window_size)
            fill.fill(colors['BLACK'])
            display.blit(fill, (0, 0))

            for (x, y), val in visited.items():
                if val:
                    # text = font.render(
                    #     str(self.risks[x][y]), True, colors['WHITE'])
                    pygame.draw.rect(
                        display, colors['BLUE'], (x*tile_size+1, y*tile_size+1, tile_size-2, tile_size-2))
                    # display.blit(text, (x*tile_size, y*tile_size))
                else:

                    # text = font.render(
                    # str(self.risks[x][y]), True, colors['BLUE'])
                    # display.blit(text, (x*tile_size, y*tile_size))
                    pygame.draw.rect(
                        display, colors['WHITE'], (x*tile_size+1, y*tile_size+1, tile_size-2, tile_size-2))


            self.pygame_low_risk()
            self.pygame_time_display()
            pygame.display.update()

    def pygame_update_only(self, pos, visited):
        if use_pygame:
            global tick
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Wheel Down / Speed up
                        if tick == 0:
                            pass
                        elif tick > 240:
                            tick = 0
                        else:
                            if tick > 30:
                                tick += 5
                            else:
                                tick += 1
                    elif event.button == 5:  # Wheel Up / Slow down
                        if tick == 1:
                            pass
                        elif tick == 0:
                            tick = 240
                        else:
                            if tick > 30:
                                tick -= 5
                            else:
                                tick -= 1
                    pygame.time.Clock().tick(tick)
            x, y = pos
            black_tile = pygame.Surface((tile_size-2, tile_size-2))
            black_tile.fill(colors['WHITE'])
            display.blit(black_tile, (x*tile_size+1, y*tile_size+1))
            if visited[pos]:
                # text = font.render(
                #     str(self.risks[x][y]), True, colors['WHITE'])
                pygame.draw.rect(
                    display, colors['BLUE'], (x*tile_size+1, y*tile_size+1, tile_size-2, tile_size-2))

            else:
                # text = font.render(
                #     str(self.risks[x][y]), True, colors['BLUE'])
                pygame.draw.rect(
                    display, colors['WHITE'], (x*tile_size+1, y*tile_size+1, tile_size-2, tile_size-2))

            # display.blit(text, (x*tile_size, y*tile_size))
            pygame.display.update()


def main():
    t1 = time()

    with open("2021/Day_15/" + input_file) as f:
        risks = [list(map(int, list(line))) for line in f.read().splitlines()]

    solution = Solution(risks)
    solution.run()
    print(solution.lowest_risk-solution.values[0][0])
    # pprint(solution.risks)

    print("Time:", time() - t1)


main()
print(computer_time/7.2)
pygame.quit()
