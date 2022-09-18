from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    x1el = browser.find_element(By.ID, "num1")
    x1 = x1el.text
    x2el = browser.find_element(By.ID, "num2")
    x2 = x2el.text
    y = str(int(x1)+int(x2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
