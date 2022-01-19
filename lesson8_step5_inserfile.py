from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Sun")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Shine")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("sunshine@gm.com")

    with open("test.txt", "w") as file:
         content = file.write("automationbypython")  # create test.txt file

    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

