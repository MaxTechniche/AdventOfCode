#!/usr/bin/env python

import os
import sys
import time
import shutil


def make_year(year, overwrite=False, auto=False):
    year = str(year)
    if overwrite is True:
        if year in os.listdir():
            print(f"Overwriting year {year}")
            shutil.rmtree(year)
            print("Done")
        os.mkdir(year)
        return

    if year not in os.listdir():
        print(f"Year {year} not found.")

        if auto is True:
            print(f"Creating year {year}...")
            os.mkdir(year)
            print("Done")
            return

        while True:
            create = input(f"Create year {year}? [y]/n: ") or "y"
            if create == "y":
                print(f"Creating year {year}...")
                os.mkdir(year)
                print("Done")
                break
            elif create == "n":
                print("Exiting...")
                sys.exit()
            else:
                print(f"{create} not a valid command")


def make_day(day, year, overwrite=False, auto=False, options=None):
    if options is None:
        options = dict()
        options["get_input"] = False
        options["get_question"] = False
        options["copy"] = False
        options["reset_solution"] = False
        options["sample_input"] = False

    os.chdir(str(year))
    day = "Day_" + str(day).zfill(2)

    if overwrite is True:
        reset_solution = True
        if day in os.listdir():
            print(f"Overwriting day {day}")
            shutil.rmtree(day)
            print("Done")
        os.mkdir(day)

    elif auto is True:
        if options['copy'] is True:
            if day not in os.listdir():
                reset_solution = True
                print(f"Creating day {day}...")
                os.mkdir(day)
                print("Done")
            elif overwrite is True:
                reset_solution = True
                print(f"Overwriting day {day}")
                shutil.rmtree(day)
                print("Done")
                os.mkdir(day)

    elif day not in os.listdir():
        print(f"Day {day} not found.")
        while True:
            create = input("Would you like to create {day}? [y]/n: ".format(
                day=day)) or "y"
            if create == "y":
                print("Creating day {day}...".format(day=day))
                os.mkdir(day)
                print("Done")
                break
            elif create == "n":
                print("Exiting...")
                sys.exit()
            else:
                print("{create} not a valid command".format(create=create))

    else:
        print("{day} already in {year}".format(day=day, year=year))
        while True:
            create = input(
                "Would you like to overwrite {day} {year}? [n]/YES: ".format(
                    day=day, year=year)) or "n"
            if create == "YES":
                print("Overwriting day {day}...".format(day=day))
                shutil.rmtree(day)
                os.mkdir(day)
                print("Done")
                break
            elif create == "n":
                print("Exiting...")
                sys.exit()
            else:
                print("{create} not a valid command".format(create=create))
        options['get_question'] = True
        options['get_input'] = True
        options['sample_input'] = True

    if day not in os.listdir():
        os.mkdir(day)
    os.chdir(day)

    if options['get_question'] is True:
        open("question.html", "w+").close()
    if options['get_input'] is True:
        open("input.txt", "w+").close()

    if options['sample_input'] is True:
        open("sample_input.txt", "w+").close()

    if options['reset_solution'] is True or ("solution.py" not in os.listdir() and options['copy'] is True):
        # copy template
        with open(os.path.join(sys.path[0], "template.txt"), "r") as template:
            with open("solution.py", "w") as solution:
                solution.write(
                    template.read().format(
                        year=year, day=day).replace("%%", "{:.3f}"))
    os.chdir("../..")


def get_year(year='current', auto=False):
    cur_year = time.strftime("%Y")
    if auto:
        if year == 'current':
            return cur_year
        elif year == 'previous':
            return str(int(cur_year) - 1)
        return cur_year

    while True:
        year = input(
            "Year [{cur_year}]: ".format(cur_year=cur_year)) or cur_year
        try:
            if 2015 > int(year) or int(year) > int(cur_year):
                print(
                    "Year not in range (2015 - {cur_year})".format(
                        cur_year=cur_year))
            else:
                return str(year)
        except ValueError:
            print("Unable to convert year to integer. Try again.")


def get_day(auto=False):
    if auto:
        return time.strftime("%d")
    while True:
        cur_day = input("Day number: ")
        try:
            if int(cur_day) > 25 or int(cur_day) < 1:
                print("Number is not in range (1-25)")
                continue
            return str(cur_day)
        except ValueError:
            print("Unable to convert day to integer. Try again.")


def main():
    cur_year = int(time.strftime("%Y")) - 1
    cur_month = time.strftime("%m")

    if cur_month in ("11", "12"):
        cur_year += 1

    year = get_year(cur_year)
    day = get_day()

    make_year(year)
    print(f"Entering year {year}")

    make_day(day, year)


if __name__ == "__main__":
    main()
