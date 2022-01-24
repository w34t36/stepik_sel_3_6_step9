import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_elements_by_class_name("btn.btn-lg.btn-primary")
    assert button, 'Button is not found'