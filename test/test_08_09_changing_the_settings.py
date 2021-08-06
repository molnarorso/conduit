from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
from data import *


class TestChangeSettings(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get(URL)
        self.driver.maximize_window()
        conduit_login(self.driver)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[@href='#/settings']").click()
        self.driver.implicitly_wait(2)

    def teardown(self):
        time.sleep(0.5)
        self.driver.quit()

    # Test No.8: Change original username
    def test_change_username(self):
        self.driver.find_element_by_xpath("//input[@placeholder='Your username']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Your username']").send_keys(new_username)
        self.driver.find_element_by_xpath("//button[normalize-space()='Update Settings']").click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element_by_xpath("//div[@class='swal-title']").text == "Update successful!"
        self.driver.find_element_by_xpath("//button[normalize-space()='OK']").click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text == new_username

    # Test No.9: Add biography
    def test_add_biography(self):
        self.driver.find_element_by_xpath("//textarea[@placeholder='Short bio about you']").clear()
        biography_text = "This is my short biography"
        self.driver.find_element_by_xpath("//textarea[@placeholder='Short bio about you']").send_keys(biography_text)
        self.driver.find_element_by_xpath("//button[normalize-space()='Update Settings']").click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element_by_xpath("//div[@class='swal-title']").text == "Update successful!"
        self.driver.find_element_by_xpath("//button[normalize-space()='OK']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//textarea[@placeholder='Short bio about you']").send_keys(Keys.CONTROL, "a")
        self.driver.find_element_by_xpath("//textarea[@placeholder='Short bio about you']").send_keys(Keys.CONTROL, "c")
        bio_to_be_saved = pyperclip.paste()
        assert bio_to_be_saved == biography_text
