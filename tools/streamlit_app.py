import os
import time
import locale
import requests
import get_all_days
import streamlit as st

from secrets import token_urlsafe
from zipfile import ZipFile
from datetime import datetime
from pytz import timezone
from streamlit_autorefresh import st_autorefresh

if "ST_SESSION_ID" not in st.session_state:
    st.session_state['ST_SESSION_ID'] = token_urlsafe(16)
if 'progress' not in st.session_state:
    st.session_state['progress'] = None
# st.write("Session ID:", st.session_state['ST_SESSION_ID'])

# st_autorefresh(interval=1000, key="refresher")
current_time = datetime.now(timezone('US/Eastern'))
current_time = datetime(2019, 12, 1, 0, 0, 0, 0, timezone('US/Eastern'))

year_max = current_time.year
if current_time.month == 12:
    year_max += 1
selectable_years = range(2015, year_max)
containers = dict()

st.write("# [`Advent of Code`](https://adventofcode.com) Day Downloader")
st.write("##### Retrieve question and/or input for selected day(s) from selected year(s).")
st.write(f"###### Current time: {current_time.strftime('%c')} (US/Eastern) (your locale: {locale.getlocale()})")


def check_available(year, day=None):
    if year < current_time.year:
        return True

    if year > current_time.year:
        return False

    if current_time.month < 12:
        return False

    if day is None:
        return True

    if current_time.day >= day:
        return True

    return False
    


def flip_year_state(year, container):
    checked = st.session_state[year]
    for day in range(1, 26):
        available = check_available(year, day)
        if available:
            st.session_state[f"{year}-{day}"] = checked


def get_num_days_available(year):
    if current_time.year > year:
        return 25
    num_days_available = 0
    for day in range(1, 26):
            if check_available(year, day):
                num_days_available += 1
    return num_days_available


def get_count_of_selections():
    count = 0
    for year in selectable_years:
        if year in st.session_state:
            for day in range(1, get_num_days_available(year) + 1):
                if f"{year}-{day}" in st.session_state:
                    if st.session_state[f"{year}-{day}"]:
                        count += 1
    return count


def sidebar_years(years, container=st.sidebar):
    for year in years:
        available = check_available(year)
        num_days_available = get_num_days_available(year)
        
        count = 0
        for day in range(1, num_days_available + 1):
            if f"{year}-{day}" in st.session_state:
                if st.session_state[f"{year}-{day}"]:
                    count += 1
        
        if year in st.session_state:
            if count == num_days_available:
                checked = True
            else:
                checked = False
        else:
            checked = False

        year_checkbox = container.checkbox(f"{year}", key=year, value=checked, on_change=flip_year_state, args=(year, container))
        if available:
            containers[year] = container.expander(f"{year}")


def sidebar_days(year, container):
    for day in range(1, 26):
        available = check_available(year, day)
        if available:
            if f"{year}-{day}" in st.session_state:
                checked = st.session_state[f"{year}-{day}"]
                container.checkbox(f"Day {day}", key=f"{year}-{day}", value=checked)
            else:
                if year in st.session_state:
                    checked = st.session_state[year]
                    container.checkbox(f"Day {day}", key=f"{year}-{day}", value=checked)
                else:
                    container.checkbox(f"Day {day}", key=f"{year}-{day}")


def update_table():
    day_cols = st.columns([2] + [1] * 25)
    for year in selectable_years:
        day_cols[0].write(f"##### *{year}:*")
        for day in range(1, 26):
            try:
                if st.session_state[f"{year}-{day}"]:
                    day_cols[day].write(f"##### {day}")
                else:
                    if check_available(year, day):
                        day_cols[day].write("##### -")
            except KeyError:
                pass

@st.cache(show_spinner=False, ttl=3600)
def download_day_info(
        year, 
        day, 
        input_=st.session_state.get("get-input", None), 
        question=st.session_state.get("get-question", None), 
        part=st.session_state.get("part", 1),
        session=st.session_state.get('VALID_AOC_COOKIE_SESSION', None)
    ):
    f = get_all_days.__file__
    i = '-i' if input_ else ''
    q = "-q" if question else ''
    part = ("-p " + str(part)) if part else ''

    y = '-y ' + str(year)
    d = '-d ' + str(day)

    os.system(f"python3 {f} {y} {d} {i} {q} {part} -o aoc -s {session}")


def retrieve_info():
    with st.spinner("Retrieving info..."):
        if not st.session_state['progress']:
            st.session_state['progress'] = 0
        st.session_state['total_to_download'] = get_count_of_selections()
        with ZipFile(f"{st.session_state['ST_SESSION_ID']}-aoc.zip", 'w') as zip_file:
            for year in selectable_years:
                for day in range(1, get_num_days_available(year) + 1):
                    if st.session_state[f"{year}-{day}"]:
                        print(f"DOWNLOADING DAY {day} OF YEAR {year}")
                        download_day_info(year, day)
                        if st.session_state['get-input'] is True:
                            zip_file.write(f"aoc/{year}/Day_{day:02d}/input.txt")
                        if st.session_state["get-question"] is True:
                            zip_file.write(f"aoc/{year}/Day_{day:02d}/question.html")
                        if "total_downloaded" in st.session_state:
                            st.session_state['total_downloaded'] += 1
                        else:
                            st.session_state['total_downloaded'] = 1
    st.session_state['transmission-received'] = True


def send_package():
    if f"{st.session_state['ST_SESSION_ID']}-aoc.zip" in os.listdir():
        st.write("Sending zip...")
    else:
        st.write("No zip to send?... check with the server admin")
    del st.session_state['transmission-received']
    st.session_state['progress'] = None



sidebar = st.sidebar
sidebar.write("#### Select year(s) and day(s) to download.")


sidebar_years(selectable_years)
for year, container in containers.items():
    sidebar_days(year, container)

update_table()

st.text_input("Advent of Code session value:", key="AOC_COOKIE_SESSION", type="password")

if "VALID_AOC_COOKIE_SESSION" not in st.session_state:
    if st.session_state["AOC_COOKIE_SESSION"] != "":
        response = requests.get("https://adventofcode.com/2015/day/1/input", cookies={"session": st.session_state["AOC_COOKIE_SESSION"]})
        if response.status_code == 200:
            st.session_state["VALID_AOC_COOKIE_SESSION"] = st.session_state["AOC_COOKIE_SESSION"]
            st.write("Valid cookie! YUM!")
        else:
            st.write(f"Invalid session. status_code: {response.status_code}")
            if response.status_code == 500:
                st.write("Mostly likely because the session cookie is not formatted correctly.")
else:
    if st.session_state["AOC_COOKIE_SESSION"] != st.session_state["VALID_AOC_COOKIE_SESSION"]:
        st.write("Cookie session changed! Revalidating...")
        del st.session_state["VALID_AOC_COOKIE_SESSION"]
    else:
        st.write("Valid cookie! YUM!")

st.write(f"##### {get_count_of_selections()} selected")
st.session_state['bottom_container'] = st.container()
if st.session_state['progress'] is None:
    selected = get_count_of_selections()
    if (selected > 0) and 'VALID_AOC_COOKIE_SESSION' in st.session_state:
        button, input_, question, part_txt, part_slider, *_ = st.columns([3, 4, 4, 2, 3, 1])

        retrieve_available = False
        if "get-input" in st.session_state:
            if st.session_state['get-input'] is True: 
                retrieve_available = True
        if "get-question" in st.session_state:
            if st.session_state['get-question'] is True:
                retrieve_available = True
        
        if retrieve_available:
            button.button("Retrieve", key="retrieve", on_click=retrieve_info)
        else:
            button.button("Retrieve", key="retrieve", on_click=retrieve_info, disabled=True)

        input_.checkbox("Personal Input?", key="get-input")
        question.checkbox("Question", key="get-question")

        if st.session_state['get-question']:
            part_txt.write("Part:")
            part_slider.slider("", key="part", min_value=1, max_value=2, value=1, label_visibility="collapsed")


if 'transmission-received' in st.session_state:
    with open(f"{st.session_state['ST_SESSION_ID']}-aoc.zip", 'rb') as zipped_file:
        st.download_button(label="Download", data=zipped_file, file_name=f"{st.session_state['ST_SESSION_ID']}-aoc.zip", mime="application/zip", on_click=send_package)




