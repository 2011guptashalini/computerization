from selenium import webdriver
from driver.constants import FIREFOX, CHROME


class SeleniumDriver:
    def __init__(self, browser=FIREFOX, chrome_driver_path=''):
        self.browser = browser
        if self.browser == FIREFOX:
            self.driver = webdriver.Firefox()

        if self.browser == CHROME:
            self.driver = webdriver.Chrome(chrome_driver_path)
