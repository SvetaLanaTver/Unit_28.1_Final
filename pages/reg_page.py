from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import AuthLocators
import time


class RegPage(BasePage):
    def __init__(self, driver, timeout=40):
        super().__init__(driver, timeout)

        url = "https://b2c.passport.rt.ru"
        # https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=6104a833-5770-464c-be72-e05af74ebdf6&theme&auth_type
        driver.get(url)
        driver.find_element(*AuthLocators.auth_reg_link).click()

        self.name_field = driver.find_element(*AuthLocators.reg_name_field)
        self.name_field_text = driver.find_element(*AuthLocators.reg_name_field_text)
        self.last_name_field_text = driver.find_element(*AuthLocators.reg_last_name_field_text)
        self.region_field_text = driver.find_element(*AuthLocators.reg_region_field_text)
        self.email_or_mobile_phone_field_text = driver.find_element(*AuthLocators.reg_email_or_mobile_phone_field_text)
        self.password_field = driver.find_element(*AuthLocators.reg_password_field)
        self.password_field_text = driver.find_element(*AuthLocators.reg_password_field_text)
        self.password_confirmation_field_text = driver.find_element(*AuthLocators.reg_password_confirmation_field_text)
        self.page_continue_button = driver.find_element(*AuthLocators.reg_page_continue_button)
        self.page_reg_text = driver.find_element(*AuthLocators.reg_page_reg_text)

    def reg_name_field_send(self, driver, str):
        driver.implicitly_wait(3)
        # Вставка строки в поле Имя
        self.name_field.send_keys(str)
        self.page_continue_button.click()

        try:
            self.error_message_name = driver.find_element(*AuthLocators.reg_error_message_name)
            return self.error_message_name.text
        except NoSuchElementException:
            return "Тест позитивный. Сообщения об ошибке нет"

    def reg_password_field_send(self, driver, str):
        driver.implicitly_wait(3)
        # Вставка строки в поле Пароль
        self.password_field.send_keys(str)
        self.page_continue_button.click()
        try:
            self.error_message_password = driver.find_element(*AuthLocators.reg_error_message_password)
            return self.error_message_password.text
        except NoSuchElementException:
            return "Тест позитивный. Сообщения об ошибке нет"

