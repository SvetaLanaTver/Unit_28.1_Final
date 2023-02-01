from .base_page import BasePage
from .locators import AuthLocators
from settings import *
from selenium.common.exceptions import NoSuchElementException
import time


class AuthPage(BasePage):

    def __init__(self, driver, timeout=40):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru"
        # https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=6104a833-5770-464c-be72-e05af74ebdf6&theme&auth_type
        driver.get(url)

        # создаем нужные элементы
        self.phone = driver.find_element(*AuthLocators.auth_phone)
        self.password = driver.find_element(*AuthLocators.auth_password)
        self.btn_login = driver.find_element(*AuthLocators.auth_btn_login)
        self.reg_link = driver.find_element(*AuthLocators.auth_reg_link)
        self.title = driver.find_element(*AuthLocators.auth_title)
        self.tab_phone = driver.find_element(*AuthLocators.auth_tab_phone)
        self.tab_mail = driver.find_element(*AuthLocators.auth_tab_mail)
        self.tab_login = driver.find_element(*AuthLocators.auth_tab_login)
        self.tab_ls = driver.find_element(*AuthLocators.auth_tab_ls)
        self.forget_password_link = driver.find_element(*AuthLocators.auth_forget_pass_link)
        self.personal_account = driver.find_element(*AuthLocators.auth_personal_account)

    def enter_personal_account(self, driver, value):
        self.personal_account.send_keys(value)

    def enter_pass(self, driver, value):
        self.password.send_keys(value)

    def refresh_page(self):
        self.driver.refresh()

    def enter_login_or_password(self, driver, log, passw):
        self.personal_account.click()  # активировали поле для ввода Лицевого счета
        self.enter_personal_account(self, log)

        self.password.click()  # активировали поле для ввода пароля
        self.enter_pass(self, passw)  # ввод пароля
        time.sleep(20) # для ручного ввода символов с картинки (капча)

        self.btn_login.click()  # клик на кнопку Войти

        # т.к. страница сайта обновилась и ссылки устарели, обновляем необходимые
        self.forget_password_link = driver.find_element(*AuthLocators.auth_forget_pass_link)
#        self.btn_login = driver.find_element(*AuthLocators.auth_btn_login)

        try:
            self.error_message_passw = driver.find_element(*AuthLocators.auth_error_message_passw)
            return self.error_message_passw.text
        except NoSuchElementException:
            return "Нет реакции на некорректный пароль или логин"
