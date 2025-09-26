from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverConstructor:
    def __init__(self):
        options = Options()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options)
    def get_driver(self):
        return self.driver