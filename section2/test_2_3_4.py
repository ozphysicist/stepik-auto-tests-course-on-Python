from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element_by_css_selector("button.btn")
    button_1.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_1 = browser.find_element_by_id('answer')
    input_1.send_keys(y)

    button_2 = browser.find_element_by_css_selector("button.btn")
    button_2.click()


    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()