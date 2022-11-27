from time import time
import numpy as np
from cProfile import run


class Cuboid:
    def __init__(self, on, x_range, y_range, z_range) -> None:
        self.on = on
        self.x1, self.x2 = x_range
        # self.x2 += 1
        self.y1, self.y2 = y_range
        # self.y2 += 1
        self.z1, self.z2 = z_range
        # self.z2 += 1

        self.volume = self.get_volume()

    def __repr__(self):
        s = ''
        s += 'x=' + str(self.x1) + '..' + str(self.x2) + ', '
        s += 'y=' + str(self.y1) + '..' + str(self.y2) + ', '
        s += 'z=' + str(self.z1) + '..' + str(self.z2) + ', '
        s += 'vol=' + str(self.volume) + ', '
        s += str(self.on)

        return s

    def get_volume(self):
        x = max(0, (self.x2 - self.x1) + 1)
        y = max(0, (self.y2 - self.y1) + 1)
        z = max(0, (self.z2 - self.z1) + 1)
        return x * y * z

    def split(self, chunk):
        x1, y1, z1 = None, None, None
        print(self)
        print(chunk)
        print('')
        total_volume = 0
        mini_cubes = []

        prev_x = self.x1
        for x in [max(chunk.x1, self.x1), min(chunk.x2, self.x2), self.x2]:
            x1 = prev_x
            x2 = x
            prev_x = x
            if x2 == chunk.x1:
                x2 -= 1
            if x1 == chunk.x2:
                x1 += 1

            prev_y = self.y1
            for y in [max(chunk.y1, self.y1), min(chunk.y2, self.y2), self.y2]:
                y1 = prev_y
                y2 = y
                prev_y = y
                if y2 == chunk.y1:
                    y2 -= 1
                if y1 == chunk.y2:
                    y1 += 1

                prev_z = self.z1
                for z in [max(chunk.z1, self.z1), min(chunk.z2, self.z2), self.z2]:
                    z1 = prev_z
                    z2 = z
                    prev_z = z
                    if z2 == chunk.z1:
                        z2 -= 1
                    if z1 == chunk.z2:
                        z1 += 1

                    mini_cube = Cuboid(True,
                                       (x1, x2),
                                       (y1, y2),
                                       (z1, z2))

                    # print(mini_cube.intersects(chunk))
                    if mini_cube.intersects(chunk) or mini_cube.volume == 0:
                        continue
                    
                    if not mini_cube.intersects(self):
                        continue
                    
                    
                    print(mini_cube)
                    mini_cubes.append(mini_cube)
                    total_volume += mini_cube.volume

        print('Total Volume of split cubes: ' + str(total_volume))

        print('')
        return mini_cubes

    def intersects(self, chunk):
        # X
        if chunk.x1 in range(self.x1, self.x2+1) \
                or chunk.x2 in range(self.x1, self.x2+1):
            # Y
            if chunk.y1 in range(self.y1, self.y2+1) \
                    or chunk.y2 in range(self.y1, self.y2+1):
                # Z
                if chunk.z1 in range(self.z1, self.z2+1) \
                        or chunk.z2 in range(self.z1, self.z2+1):
                    return True

        return False

        # convert each intersection into a cuboid


def parse(step, offset=0):
    o, step = step.split()
    o = True if o == 'on' else False
    x, y, z = step.split(',')
    x = x.split('..')
    y = y.split('..')
    z = z.split('..')

    x[0] = x[0][2:]
    x = [xn+offset for xn in map(int, x)]
    y[0] = y[0][2:]
    y = [yn+offset for yn in map(int, y)]
    z[0] = z[0][2:]
    z = [zn+offset for zn in map(int, z)]

    return o, x, y, z


def main():
    inters = 0
    t1 = time()

    with open("2021/Day_22/sample_input") as f:
        steps = f.read().splitlines()

    cuboids = set([Cuboid(*parse(steps[0]))])

    for step in steps[1:]:
        new_cuboid = Cuboid(*parse(step))
        if new_cuboid.on:
            cuboids.add(new_cuboid)
            continue

        for cuboid in cuboids.copy():
            if cuboid.intersects(new_cuboid):
                inters += 1
                for mini_cube in cuboid.split(new_cuboid):
                    cuboids.add(mini_cube)
                cuboids.remove(cuboid)

    lit_cubes = set([])
    for cuboid in cuboids:
        for x in range(cuboid.x1, cuboid.x2+1):
            for y in range(cuboid.y1, cuboid.y2+1):
                for z in range(cuboid.z1, cuboid.z2+1):
                    lit_cubes.add((x, y, z))

    print(len(lit_cubes))
    # assert len(lit_cubes) == 590784
    print("Time:", time() - t1)


main()
# run('main()')
