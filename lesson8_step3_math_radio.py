from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    t_num1 = int(num1.text)

    num2 = browser.find_element_by_id("num2")
    t_num2 = int(num2.text)

    x = str(t_num1+t_num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

