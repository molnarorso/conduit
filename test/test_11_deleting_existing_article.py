from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from data import *


class TestDeleteArticle(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get(URL)
        self.driver.maximize_window()
        conduit_login(self.driver)
        self.driver.implicitly_wait(5)
        create_new_article(self.driver)

    def teardown(self):
        time.sleep(0.5)
        self.driver.quit()

    # Test No.11: Deleting existing article
    def test_delete_article(self):
        self.driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']//span[1]").click()
        time.sleep(2)
        assert self.driver.current_url == "http://localhost:1667/#/"
        element_does_not_exist_by_link_text(self.driver, "Single article")
