import time

import random
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        submit_button = self.element_is_visible(TextBoxPageLocators.SUBMIT)
        self.go_to_element(submit_button)
        submit_button.click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.get_text_content(self.locators.CREATED_FULL_NAME).split(':')[1]
        email = self.get_text_content(self.locators.CREATED_EMAIL).split(':')[1]
        current_address = self.get_text_content(self.locators.CREATED_CURRENT_ADDRESS).split(':')[1]
        permanent_address = self.get_text_content(self.locators.CREATED_PERMANENT_ADDRESS).split(':')[1]

        return full_name, email, current_address, permanent_address

    def get_text_content(self, locator):
        try:
            element = self.element_is_present(locator)
            return element.text.strip()
        except NoSuchElementException:
            return None


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()
    
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self,):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count !=0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(xpath,self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(" ", "").replace("doc", "").replace(".", "").lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(" ", "").lower()
