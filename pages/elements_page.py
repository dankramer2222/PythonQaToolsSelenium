import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Dan")
        self.element_is_visible(self.locators.EMAIL).send_keys("test@gmail.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("12street")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("13street")
        submit_button = self.element_is_visible(TextBoxPageLocators.SUBMIT)
        self.go_to_element(submit_button)
        submit_button.click()

    def check_filled_form(self):
        full_name = self.get_text_content(self.locators.CREATED_FULL_NAME)
        email = self.get_text_content(self.locators.CREATED_EMAIL)
        current_address = self.get_text_content(self.locators.CREATED_CURRENT_ADDRESS)
        permanent_address = self.get_text_content(self.locators.CREATED_PERMANENT_ADDRESS)

        return full_name, email, current_address, permanent_address

    def get_text_content(self, locator):
        try:
            element = self.element_is_present(locator)
            return element.text.strip()
        except NoSuchElementException:
            return None

