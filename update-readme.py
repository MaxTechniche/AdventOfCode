from selenium import webdriver
from selenium.webdriver import firefox, chrome
import time
import os
from PIL import Image
from dotenv import load_dotenv
import sys


load_dotenv()
SESSION_ID = os.environ.get('SESSION_ID')
BASE_WEB_URL = os.environ.get('BASE_WEB_URL')


if not BASE_WEB_URL.endswith('/'):
    BASE_WEB_URL += '/'

options = chrome.options.Options()
options.add_argument('--headless')

# service = chrome.service.Service('/mnt/c/Users/maxte/Downloads/chromedriver.exe
# service = chrome.service.Service('localhost:9515')

service = chrome.service.Service('/mnt/c/Users/maxte/Downloads/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

if WINDOW_SIZE := os.environ.get("WINDOW_SIZE"):
    driver.set_window_size(*WINDOW_SIZE.split(","))
if WINDOW_POSITION := os.environ.get("WINDOW_POSITION"):
    driver.set_window_position(*WINDOW_POSITION.split(","))

driver.get(BASE_WEB_URL)
driver.add_cookie({"name": "session", "value": SESSION_ID})

YEAR = '2015'

driver.get(BASE_WEB_URL + YEAR)
driver.save_screenshot(filename=f'{WINDOW_SIZE}.png')

driver.quit()

with Image.open(f'{WINDOW_SIZE}.png') as img:

    Image.Image.crop(img, (0, 85, 640, 785)).save(f'{WINDOW_SIZE}.png')