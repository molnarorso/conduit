from selenium.common.exceptions import NoSuchElementException
import pytest

URL = "http://localhost:1667/"

original_username = "Molnár Orsolya"
new_username = str("Kovács Margit")
fix_email = "somebody@freemail.hu"
non_complying_password = "badpassword"
complying_password = "GoodPassword1"
wrong_password = "Wrongpassword"

article_text = "I do not have much to say about birds"

new_article_title = "Not a single article"
new_article_about = "Not a single topic"
new_article_text = "Now this single article has changed"
new_article_tag = "not single"


def conduit_login(driver):
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
    driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(fix_email)
    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(complying_password)
    driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
    driver.implicitly_wait(2)


def element_does_not_exist_by_xpath(driver, xpath):
    with pytest.raises(NoSuchElementException):
        driver.find_element_by_xpath(xpath)


def element_does_not_exist_by_link_text(driver, link_text):
    with pytest.raises(NoSuchElementException):
        driver.find_element_by_xpath(link_text)


def create_new_article(driver):
    driver.find_element_by_xpath("//a[@href='#/editor']").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//input[@placeholder='Article Title']").send_keys("Single article")
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys("Single topic")
    driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys("This is a single article about a single article")
    driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("single")
    driver.find_element_by_xpath("//button[normalize-space()='Publish Article']").click()
    driver.implicitly_wait(2)

