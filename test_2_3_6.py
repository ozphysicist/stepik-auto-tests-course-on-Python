from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element_by_css_selector('button.trollface.btn')
    button_1.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_1 = browser.find_element_by_id('answer')
    input_1.send_keys(y)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()