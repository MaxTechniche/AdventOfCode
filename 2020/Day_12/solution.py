from time import time

t1 = time()

with open("2020/Day_12/input") as f:
    directions = {
        i: {"direction": x[0], "change": int(x[1:])}
        for i, x in enumerate(f.read().splitlines())
    }

degrees = {"N": 270, "E": 0, "S": 90, "W": 180}
dirs = {deg: direct for direct, deg in degrees.items()}


def move_waypoint(lat, long, change, direction=None):
    if direction == "N":
        lat += change
    elif direction == "E":
        long += change
    elif direction == "S":
        lat -= change
    elif direction == "W":
        long -= change

    return lat, long


def rotate(value, current_direction):
    way, change = value.values()
    val = (degrees[current_direction] + (way == "R" or -1) * change) % 360
    return dirs[val]


current_direction = "E"
lat = long = 0

for i, val in directions.items():
    if val["direction"] in ["R", "L"]:
        current_direction = rotate(val, current_direction)
    elif val["direction"] == "F":
        lat, long = move_waypoint(lat, long, val["change"], current_direction)
    else:
        lat, long = move_waypoint(lat, long, val["change"], val["direction"])

print("Part 1:", abs(lat) + abs(long))


point_lat, point_long = 1, 10
ship_lat, ship_long = 0, 0


def rotate_waypoint(val):
    lat = point_lat - ship_lat
    long = point_long - ship_long
    direction, change = val.values()
    for x in range(change % 360 // 90):
        if direction == "R":
            lat, long = -long, lat
        elif direction == "L":
            lat, long = long, -lat

    return ship_lat + lat, ship_long + long


def move_ship_and_waypoint(val):
    lat = point_lat - ship_lat
    long = point_long - ship_long
    track_lat, track_long = ship_lat, ship_long
    for x in range(val):
        track_lat += lat
        track_long += long

    return track_lat, track_long, track_lat + lat, track_long + long


for i, val in directions.items():
    if val["direction"] in ["R", "L"]:
        point_lat, point_long = rotate_waypoint(val)
        continue
    elif val["direction"] == "F":
        ship_lat, ship_long, point_lat, point_long = move_ship_and_waypoint(
            val["change"]
        )
    else:
        point_lat, point_long = move_waypoint(
            point_lat, point_long, val["change"], val["direction"]
        )

print("Part 2:", abs(ship_lat) + abs(ship_long))

print("Time:", time() - t1)  # .005
