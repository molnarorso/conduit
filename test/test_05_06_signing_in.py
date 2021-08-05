from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from data import *


class TestSignIn(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = False
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get(URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(0.5)
        self.driver.quit()

    # Test No.5: Signing in using wrong password
    def test_sign_in_with_wrong_password(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(new_email)
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(wrong_password)
        self.driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath("//div[@class='swal-title']").text == "Login failed!"
        self.driver.find_element_by_xpath("//button[normalize-space()='OK']").click()

    # Test No.6: Signing in using the correct password
    def test_sign_in_with_correct_password(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(new_email)
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(complying_password)
        self.driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath("//a[@active-class='active']").is_displayed()
