from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson_id):
    link = f"https://stepik.org/lesson/{lesson_id}/step/1/"
    browser.get(link)
    answer = math.log(int(time.time()))
    input = browser.find_element(By.CSS_SELECTOR, "textarea")
    input.send_keys(str(answer))
    
