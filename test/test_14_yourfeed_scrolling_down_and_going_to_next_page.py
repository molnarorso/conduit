from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from data import *


class TestYourFeed(object):
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

    # Test No.14: Scrolling down to the bottom of "Your feed" and going to next page and back
    def test_your_feed(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[normalize-space()='Your Feed']").click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[normalize-space()='2']").click()
        assert self.driver.find_element_by_xpath("//li[@class='page-item active']").text == "2"
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[normalize-space()='1']").click()
        assert self.driver.find_element_by_xpath("//li[@class='page-item active']").text == "1"

