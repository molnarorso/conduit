import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import *


class TestCreateAndDeleteArticle(object):
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

    # Test No.10: Creating new article and saving body into separate file
    def test_create_new_article_and_saving_it(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[@href='#/editor']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Article Title']").send_keys("My birds")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys("Birds")
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(article_text)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("birds")
        self.driver.find_element_by_xpath("//button[normalize-space()='Publish Article']").click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text == article_text
        my_text_file = open('article_body.txt', 'w')
        item_to_be_saved = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text
        my_text_file.write(item_to_be_saved)
        my_text_file.close()
        self.driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']//span[1]").click()
