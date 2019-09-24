from selenium import webdriver
import time
import math

def calc(x):
    return(str(math.log(abs(12*math.sin(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    ch1 = browser.find_element_by_id("input_value")
    x = ch1.text
    x = int(x)
    y = calc(x)
    y = ("{}".format(y))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button1 = browser.find_element_by_class_name("btn.btn-primary")
    button1.click()
finally:
    time.sleep(5)
    browser.quit()
