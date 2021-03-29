import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add_button_title(browser):
    browser.get(link)
    time.sleep(30)
    busket_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(busket_button) == 1, "'Add to basket' button isn't unique or not found"