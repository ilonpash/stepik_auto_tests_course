from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    t_num1 = num1.text()

    num2 = browser.find_element_by_id("num2")
    t_num2 = num2.text()

    x = str(t_num1+t_num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x)




    x_element = browser.find_element_by_id("treasure")
    x = int(x_element.get_attribute("valuex"))
    y = calc(x)

    input_val = browser.find_element_by_css_selector("#answer")
    input_val.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

