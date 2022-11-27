from time import time
import re
from pprint import pprint


def rotateX(beacons):
    newBeacons = []
    for beacon in beacons:
        x, y, z = beacon

        newX = x
        newY = -z
        newZ = y

        newBeacons.append((newX, newY, newZ))

    return newBeacons


def rotateY(beacons):
    newBeacons = []
    for beacon in beacons:
        x, y, z = beacon

        newX = z
        newY = y
        newZ = -x

        newBeacons.append((newX, newY, newZ))

    return newBeacons


def rotateZ(beacons):
    newBeacons = []
    for beacon in beacons:
        x, y, z = beacon

        newX = -y
        newY = x
        newZ = z

        newBeacons.append((newX, newY, newZ))

    return newBeacons


def axis_rotate(beacons, functions):
    for func in functions:
        beacons = func(beacons)
    return beacons


def check_for_match(scanner1, scanner2, s1_beacon, s2_beacon):
    beacons = scanner2[1].copy()

    completed_rotations = []

    for fl in [[rotateZ], [rotateZ], [rotateZ], [rotateZ, rotateY], [rotateY, rotateY], [rotateX]]:
        cr = []
        for r in range(4):
            base_beacon = beacons[s2_beacon]
            x_change = base_beacon[0] - scanner1[1][s1_beacon][0]
            y_change = base_beacon[1] - scanner1[1][s1_beacon][1]
            z_change = base_beacon[2] - scanner1[1][s1_beacon][2]

            ts2bp = set()
            for b in beacons:
                ts2bp.add((b[0]-x_change, b[1]-y_change, b[2]-z_change))

            total = 0
            for beacon in scanner1[1]:
                if beacon in ts2bp:
                    total += 1
            if total > 11:
                completed_rotations.extend(cr)
                return list(ts2bp), (x_change, y_change, z_change)

            beacons = rotateX(beacons)
            cr.append(rotateX)

        beacons = axis_rotate(beacons, fl)
        completed_rotations.extend(fl)


def loop_beacons(s1, s2):
    for s1b in range(len(s1[1])):
        for s2b in range(len(s2[1])):
            match = check_for_match(s1, s2, s1b, s2b)
            if match:
                return s1[0], s2[0], *match


def orient_scanner(match, scanners, kso):
    s1, s2, new_beacons = match

    scanners[s2] = new_beacons

    kso.add(s1)
    kso.add(s2)

    return scanners, kso


def main():
    t1 = time()

    with open("2021/Day_19/input") as f:
        lines = f.read().split('\n\n')

    scanners = {}
    for group in lines:
        group = group.splitlines()
        s = group[0]
        s = int(re.search('\d\d?', s).group())
        beacons = [tuple(map(int, line.split(','))) for line in group[1:]]
        scanners[s] = beacons

    kso = set([0])
    relative_scanner_locations = set()

    matched = False

    while not matched:
        matched = True
        for scanner in range(len(scanners)):
            s1 = (scanner, scanners[scanner])
            if s1[0] not in kso:
                matched = False
                continue
            for scanner in range(len(scanners)):
                s2 = (scanner, scanners[scanner])
                # if s1[0] not in kso and s2[0] not in kso:
                #     matched = False
                #     continue
                # if s2[0] in kso and s1[0] not in kso:
                #     matched = False
                #     continue
                if s1[0] == s2[0]:
                    continue
                if s1[0] in kso and s2[0] in kso:
                    continue

                print(s1[0], s2[0])
                match = loop_beacons(s1, s2)
                if match:
                    print('^^^ MATCHED')
                    relative_scanner_locations.add(match[-1])
                    scanners, kso = orient_scanner(match[:-1], scanners, kso)
                    print(kso)
                    print('')

    beacons = set()
    for scanner in scanners.values():
        beacons.update(set(scanner))

    pprint(beacons)
    print(len(beacons))

    largest_distance = 0
    for scanner1 in relative_scanner_locations:
        for scanner2 in relative_scanner_locations:
            x = abs(scanner2[0] - scanner1[0])
            y = abs(scanner2[1] - scanner1[1])
            z = abs(scanner2[2] - scanner1[2])
            largest_distance = max(largest_distance, x+y+z)

    print(largest_distance)

    print("Time:", time() - t1)


main()
