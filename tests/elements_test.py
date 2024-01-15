import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from generator.generator import generated_person
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            input_checkbox = check_box_page.click_random_checkbox()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button("Yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("Impressive")
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("No")
            output_no = radio_button_page.get_output_result()

            assert output_yes == "Yes", "'Yes' have not been selected"
            assert output_impressive == "Impressive", "'Impressive' have not been selected"
            assert output_no == "No", "'No' have not been selected"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.add_new_person()
            time.sleep(5)
