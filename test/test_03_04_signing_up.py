from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from data import *


class TestSignUp(object):
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

    # Test No.3: Signing up using a non-complying password
    def test_sign_up_with_noncomplying_password(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign up']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(original_username)
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(varying_user_email)
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(non_complying_password)
        self.driver.find_element_by_xpath("//button[normalize-space()='Sign up']").click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath("//div[@class='swal-title']").text == "Registration failed!"
        self.driver.find_element_by_xpath("//button[normalize-space()='OK']").click()

    # Test No.4: Signing up using a complying password
    def test_sign_up_with_complying_password(self):
    # Signing up
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign up']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(original_username)
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(fix_email)
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(complying_password)
        self.driver.find_element_by_xpath("//button[normalize-space()='Sign up']").click()
        self.driver.implicitly_wait(10)
        assert self.driver.find_element_by_xpath("//div[@class='swal-text']").text == "Please wait..."
        time.sleep(5)
        assert self.driver.find_element_by_xpath("//div[@class='swal-text']").text == "Your registration was successful!"
        self.driver.find_element_by_xpath("//button[normalize-space()='OK']").click()
        time.sleep(2)
