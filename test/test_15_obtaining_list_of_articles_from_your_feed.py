from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from data import *


class TestListArticlesFromYourFeed(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = False
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get(URL)
        self.driver.maximize_window()
        conduit_login(self.driver)

    def teardown(self):
        time.sleep(0.5)
        # self.driver.quit()

    # Test No.15: Obtaining list of articles from "Your feed"
    def test_list_articles_from_your_feed(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[normalize-space()='Your Feed']").click()
        time.sleep(2)
        with open('article_title_list.txt', 'w') as my_file:
            my_article_title_list = self.driver.find_elements_by_xpath("//a[@class='preview-link']/h1")
            for i in my_article_title_list:
                time.sleep(0.2)
                my_file.write(i.text)
                my_file.write("\n")



