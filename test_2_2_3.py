from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = int(browser.find_element_by_id('num1').text)
    num_2 = int(browser.find_element_by_id('num2').text)

    selected_answer = str(num_1 + num_2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(selected_answer)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()