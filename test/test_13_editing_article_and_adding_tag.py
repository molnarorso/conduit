from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import *


class TestEditArticle(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get(URL)
        self.driver.maximize_window()
        conduit_login(self.driver)
        create_new_article(self.driver)

    def teardown(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/button/span').click()
        self.driver.quit()

    # Test No.13: Editing an article and adding another tag
    def test_editing_article_and_adding_tag(self):
        self.driver.find_element_by_xpath("//a[@class='btn btn-sm btn-outline-secondary']//span[1]").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Article Title']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Article Title']").send_keys(new_article_title)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys(new_article_about)
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").clear()
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(new_article_text)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys(new_article_tag)
        self.driver.find_element_by_xpath("//button[normalize-space()='Publish Article']").click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text == new_article_text
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/a[2]').text == new_article_tag