import time
from pages.base_page import BasePage
import pytest


def test(driver):
    page = BasePage(driver, "https://www.google.com")  # full url
    page.open()
    time.sleep(5)
