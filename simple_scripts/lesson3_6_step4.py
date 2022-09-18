from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_math(browser, lesson_id):
    link = f"https://stepik.org/lesson/{lesson_id}/step/1/"
    browser.get(link)
    browser.implicitly_wait(10)
    input = browser.find_element(By.CSS_SELECTOR, ".string-quiz__textarea")
    answer = math.log(int(time.time()))
    input.send_keys(str(answer))
    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button.click()
    browser.implicitly_wait(10)
    output = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    assert output.text == "Correct!", "Incorrect answer!"
