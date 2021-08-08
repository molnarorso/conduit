from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import *
import time


class TestLogout(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get(URL)
        self.driver.maximize_window()
        conduit_login(self.driver)

    def teardown(self):
        time.sleep(0.5)
        self.driver.quit()

    # Test No.7: Logout
    def test_logout(self):
        self.driver.find_element_by_xpath("//a[@active-class='active']").click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").is_displayed()

