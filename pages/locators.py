from selenium.webdriver.common.by import By

class AuthLocators:

    # страница Авторизация
    auth_phone = (By.ID, 'username') # поле для ввода телефона/почты/логина/лиц счета
    auth_password = (By.ID, 'password') # поле для ввода пароля
    auth_btn_login = (By.XPATH, '//button[@id="kc-login"]') # кнопка Войти
    auth_reg_link = (By.XPATH, "//a[@id='kc-register']") # ссылка Зарегистрироваться
    auth_title = (By.XPATH, '//*[@id="page-right"]/div/div/h1') # заголовок страницы Авторизация
    auth_tab_phone = (By.ID, 't-btn-tab-phone') # таб выбора Номер
    auth_tab_mail = (By.ID, "t-btn-tab-mail") # таб выбора Почта
    auth_tab_login = (By.ID, 't-btn-tab-login') # таб выбора Логин
    auth_tab_ls = (By.ID, 't-btn-tab-ls') # таб выбора Лицевой счет
    auth_res_pass_text = (By.XPATH, '//*[@id="page-right"]/div/div/h1') # заголовок страницы Регистрация
    auth_forget_pass_link = (By.XPATH, '//*[@id="forgot_password"]') # ссылка "Забыл пароль"
    auth_personal_account = (By.ID, "username") # поле для ввода Лицевого счета
    auth_error_message_passw = (By.XPATH, '//*[@id="page-right"]/div/div/p') #сообщение об ошибке в логине или пароле

    # на странице Регистрация
    reg_name_field = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input') # поле Имя
    reg_name_field_text = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span[2]') # надпись поля Имя
    reg_last_name_field_text = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]') # надпись поля Фамилия
    reg_region_field_text = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/span[2]') # надпись поля Регион
    reg_email_or_mobile_phone_field_text = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[2]') # надпись поля емайл или мобильный телефон
    reg_password_field = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/input') # поле Пароль
    reg_password_field_text = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]') # надпись поля Пароль
    reg_password_confirmation_field_text = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')  # надпись Подтверждение пароля
    reg_page_continue_button = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')  # кнопка Продолжить
    reg_error_message_name = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span') #сообщение об ошибке в имени
    reg_error_message_password = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span') #сообщение об ошибке в пароле
    reg_page_reg_text = (By.XPATH, '//*[@id="page-right"]/div/div/h1') # слово Регистрация

