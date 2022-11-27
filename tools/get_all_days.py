#!/usr/bin/env python3

import make_day as make_day
import re
import os
import sys
import time
import argparse

from itertools import chain
from requests import get
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()


def parse(value, t=None):
    if value == 0:
        if t == 'year':
            value = range(2015, time.localtime().tm_year + 1)
        elif t == 'day':
            value = range(1, 26)
        return value
    for i, v in enumerate(value):
        if "-" in v:
            start, end = v.split("-")
            value[i] = list(range(int(start), int(end) + 1))
        if "," in v:
            value[i] = list(map(int, v.strip(",").split(",")))
        if isinstance(value[i], str):
            value[i] = [int(value[i])]
    value = set(chain.from_iterable(value))
    return value


def get_day_info(year, day, options):
    """ This will send GET requests to the AoC website.
    If you look at the response of the website,
    you'll see that the creator has put a notice
    as to ask to reduce the amount of automated request.
    Please respect this notice,
    and use this script sparingly."""
    overwrite = False
    reset_solution = options["reset_solution"]
    auto = True
    copy_template = options["copy"]
    get_input = options["get_input"]
    get_question = options["get_question"]
    parts = options["parts"]
    session_id = options["session_id"]
    cookies = dict()

    if get_input is True or parts == 2:
        cookies["session"] = session_id

    os.chdir(options["output"])
    make_day.make_year(year, overwrite=overwrite, auto=auto)
    make_day.make_day(day, year, overwrite=overwrite, auto=auto, options=options)
    # Get the input for the day
    question_url = f"https://adventofcode.com/{year}/day/{day}"
    input_url = question_url + "/input"

    if get_input is True:
        response = get(input_url, cookies=cookies)
        if response.status_code == 200:
            with open(f"{year}/Day_{day:02d}/input.txt", "w") as f:
                f.write(response.text)
        else:
            print(f"Failed to get input for day {day}, year {year}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")

    # Get the question for the day
    if get_question is True:
        if parts == 2:
            response = get(question_url, cookies=cookies)
        else:
            response = get(question_url)
        if response.status_code == 200:
            with open(f"{year}/Day_{day:02d}/question.html", "w") as f:
                soup = BeautifulSoup(response.text, "html.parser")
                m = re.sub("<p>You can also(.|\s)*", "", str(soup.main))
                f.write(m + "</main>")
        else:
            print(f"Failed to get question for day {day}, year {year}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")
    print("Done")


def get_days_from_year(year, days, args):
    for day in days:
        print(year, day)
        get_day_info(year, day, args)
    

def main(args):
    args = vars(args)
    __location__ = os.path.abspath(args["output"])
    if not os.path.exists(__location__):
        os.makedirs(__location__)
    args["output"] = __location__
    args["base_url"] = "https://adventofcode.com"
    years = parse(args["years"], t="year")
    days = parse(args["days"], t="day")

    os.chdir(__location__)

    for year in years:
        get_days_from_year(year, days, args)

    print("Finished getting info for all days")


if __name__ == "__main__":
    cur_year = time.strftime("%Y")
    if time.strftime("%m") != "12":
        cur_year = str(int(cur_year) - 1)

    parser = argparse.ArgumentParser(
        prog="`Advent of Code` Year Grabber",
        description="Download selected `Advent of Code` days for a given year\
             or given years."
    )
    parser.add_argument(
        "-y",
        "--year",
        "--years",
        nargs="+",
        dest="years",
        default=0,
        help="The year(s) to get the days for. Can be a single year, a range of years, or a list of years separated by commas or spaces. Defaults to all years. (0)"
    )
    parser.add_argument(
        "-d",
        "--days",
        nargs="+",
        dest="days",
        default=0,
        help="Days to get. Can be a single day, a range of days, or a list of days separated by commas and/or spaces. Defaults to all days. (0)"
    )
    parser.add_argument(
        "-s",
        "--session-id",
        dest="session_id",
        default=os.getenv("SESSION_ID"),
        help="Your session ID from `adventofcode.com`. Needed to get input and part 2 question if you have solved part 1. Default is to use the SESSION_ID environment variable.",
    )
    parser.add_argument(
        "-i",
        "--input",
        "--get-input",
        dest="get_input",
        action="store_true",
        help="Will attempt to get the input for the day (must have a valid session id).",
    )
    parser.add_argument(
        "-q",
        "--question",
        "--get-question",
        dest="get_question",
        action="store_true",
        help="Will get the question for the day.",
    )
    parser.add_argument(
        "-p",
        "--parts",
        dest="parts",
        type=int,
        default=1,
        help="Will attempt to get the question for the day up to the given part. Defaults to 1",
    )
    parser.add_argument(
        "-r",
        "--reset-solution",
        dest="reset_solution",
        action="store_true",
        help="Will reset the solution file for the day (if 'solution.py' exists in day).",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        default=".",
        help="The directory to output the files to.",
    )
    parser.add_argument(
        "-c",
        "--copy",
        dest="copy",
        action="store_true",
        help="Will copy the python template.",
    )
    parser.add_argument(
        "--sample-input",
        dest="sample_input",
        action="store_true",
    )

    args = parser.parse_args()

    main(args)
