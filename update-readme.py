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

SESSION_ID = os.environ.get("SESSION_ID")
BASE_WEB_URL = "https://adventofcode.com"
# BASE_WEB_URL = os.environ.get('BASE_WEB_URL')

if BASE_WEB_URL and not BASE_WEB_URL.endswith("/"):
    BASE_WEB_URL += "/"

options = chrome.options.Options()
options.add_argument("--headless")

service = chrome.service.Service("localhost:4444")

# service = chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

if WINDOW_SIZE := os.environ.get("WINDOW_SIZE"):
    driver.set_window_size(*WINDOW_SIZE.split(","))
if WINDOW_POSITION := os.environ.get("WINDOW_POSITION"):
    driver.set_window_position(*WINDOW_POSITION.split(","))

driver.get(BASE_WEB_URL)
driver.add_cookie({"name": "session", "value": SESSION_ID})

for YEAR in range(2015, CURRENT_YEAR):
    print(f"YEAR: {YEAR}")
    YEAR = str(YEAR)
    FILENAME = f"assets/{YEAR}-starss.png"

    driver.get(BASE_WEB_URL + YEAR)
    driver.save_screenshot(filename=FILENAME)

    with Image.open(FILENAME) as img:

        if sys.platform == "darwin":
            Image.Image.crop(img, (0, 150, 1300, 1700)).save(FILENAME)
        else:
            Image.Image.crop(img, (0, 85, 640, 785)).save(FILENAME)
    print(f"Saved {FILENAME}")

driver.quit()
