import os
import sys
import time

from dotenv import load_dotenv
from PIL import Image
from selenium import webdriver
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()
CURRENT_YEAR = int(time.strftime("%Y"))
if int(time.strftime("%m")) == 12:
    CURRENT_YEAR += 1
elif int(time.strftime("%m")) == 11 and int(time.strftime("%d")) > 26:
    CURRENT_YEAR += 1

SESSION_ID = os.environ.get("SESSION_ID")
BASE_WEB_URL = "https://adventofcode.com"
WHITE_SQUARE = "assets/white-square.png"

USERNAME = os.environ.get("USERNAME", None)
USERNAME = "MaxTechniche"
if isinstance(USERNAME, str) and USERNAME != "":
    CHARACTERS = len(USERNAME)
else:
    CHARACTERS = 0

if BASE_WEB_URL and not BASE_WEB_URL.endswith("/"):
    BASE_WEB_URL += "/"

options = chrome.options.Options()
options.add_argument("--headless")

service = chrome.service.Service("localhost:4444")

# Not needed ?
# service = chrome.service.Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options, service=service)
WINDOW_SIZE = os.environ.get("WINDOW_SIZE", "1200,1000")
driver.set_window_size(*WINDOW_SIZE.split(","))

driver.get(BASE_WEB_URL)
driver.add_cookie({"name": "session", "value": SESSION_ID})

for YEAR in range(2015, CURRENT_YEAR):
    print(f"YEAR: {YEAR}", file=sys.stderr, flush=True)
    YEAR = str(YEAR)
    TOTAL_STARS_FILE = f"assets/{YEAR}-total.png"
    FILENAME = f"assets/{YEAR}-stars.png"

    driver.get(BASE_WEB_URL + YEAR)
    driver.save_screenshot(filename=FILENAME)

    with Image.open(FILENAME) as img:

        if sys.platform == "darwin":
            if CHARACTERS > 0:
                Image.Image.crop(
                    img,
                    (
                        828 * 2 + 12 * (CHARACTERS + 1),
                        25,
                        828 * 2 + 12 * (CHARACTERS + 7),
                        55,
                    ),
                ).save(TOTAL_STARS_FILE)
            else:
                Image.open(WHITE_SQUARE).save(TOTAL_STARS_FILE)
            Image.Image.crop(img, (0, 150, 1300, 1700)).save(
                FILENAME
            )
        else:
            if CHARACTERS > 0:
                Image.Image.crop(
                    img,
                    (
                        726 + 12 * (CHARACTERS + 1),
                        10,
                        726 + 12 * (CHARACTERS + 5),
                        30,
                    ),
                ).save(TOTAL_STARS_FILE)
            else:
                Image.open(WHITE_SQUARE).save(TOTAL_STARS_FILE)
            Image.Image.crop(img, (0, 85, 640, 785)).save(
                FILENAME
            )
    print(f"Saved {FILENAME}", file=sys.stderr, flush=True)

driver.quit()
