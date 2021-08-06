import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
from data import *


class TestCreateMultipleArticles(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get(URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        conduit_login(self.driver)

    def teardown(self):
        time.sleep(0.5)
        self.driver.quit()

    # Test No.12: Creating multiple articles
    def test_create_multiple_articles(self):
        with open('multiple_articles.csv', newline='') as articles_source_file:
            reader = csv.DictReader(articles_source_file)
            for row in reader:
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath("//a[@href='#/editor']").click()
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath("//input[@placeholder='Article Title']").clear()
                self.driver.find_element_by_xpath("//input[@placeholder='Article Title']").send_keys(row['Title'])
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').clear()
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys(row['About'])
                self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").clear()
                self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(row['Content'])
                self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys(row['Tag'])
                self.driver.find_element_by_xpath("//button[normalize-space()='Publish Article']").click()
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath("//a[normalize-space()='Home']").click()
                self.driver.implicitly_wait(5)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                self.driver.implicitly_wait(5)
                assert self.driver.find_element_by_partial_link_text(row['Title']).is_displayed()
            with open('multiple_articles.csv', newline='') as deletion_source_file:
                deletion_reader = csv.DictReader(deletion_source_file)
                for row1 in deletion_reader:
                    time.sleep(3)
                    self.driver.find_element_by_partial_link_text(row1['Title']).click()
                    self.driver.implicitly_wait(5)
                    self.driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']//span[1]").click()
                    self.driver.implicitly_wait(5)

