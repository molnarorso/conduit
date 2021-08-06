from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from data import *


class TestCookies(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get(URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(0.5)
        self.driver.quit()

    # Test No.1: Declining cookies
    def test_declining_cookies(self):
        self.driver.find_element_by_xpath("//div[normalize-space()='I decline!']").click()
        time.sleep(0.5)
        test_element_does_not_exist_by_xpath(self.driver, "//div[normalize-space()='I decline!']")

    # Test No.2: Accepting cookies
    def test_accepting_cookies(self):
        self.driver.find_element_by_xpath("//div[normalize-space()='I accept!']").click()
        time.sleep(0.5)
        test_element_does_not_exist_by_xpath(self.driver, "//div[normalize-space()='I accept!']")

