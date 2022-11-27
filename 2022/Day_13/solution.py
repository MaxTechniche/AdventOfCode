from time import perf_counter


def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        print("Time: {:.3f} seconds".format(time_delta))
    return wrapper()


def main():
    with open("2022/Day_13/input") as f:
        lines = f.read().splitlines()


if __name__ == "__main__":
    format_time(main)
