from urllib.parse import urlparse

class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=40):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    # Метод get_relative_link возвращает относительный путь до текущей страницы (без домена). 
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def find_el(self, by, location):
        return self.driver.find_element(by, location)


