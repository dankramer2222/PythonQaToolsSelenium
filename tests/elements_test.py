import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name doesn't match"
            assert email == output_email, "the email name doesn't match"
            assert current_address.replace("\n", " ") == output_cur_addr, "the current address name doesn't match"
            assert permanent_address.replace("\n", " ") == output_per_addr, "the permanent address name doesn't match"


