from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    
    input_name = browser.find_element_by_css_selector('[name = "firstname"]')
    input_name.send_keys('Olga')

    input_last_name = browser.find_element_by_css_selector('[name = "lastname"]')
    input_last_name.send_keys('Z')

    input_email = browser.find_element_by_css_selector('[name = "email"]')
    input_email.send_keys('oz@test.com')

    input_file = browser.find_element_by_id('file')
    input_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()