from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_1 = browser.find_element_by_id('answer')
    input_1.send_keys(y)

    input_2 = browser.find_element_by_id('robotCheckbox')
    input_2.click()

    input_3 = browser.find_element_by_id('robotsRule')
    input_3.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()