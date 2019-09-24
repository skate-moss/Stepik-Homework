from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return (str(math.log(abs(12 * math.sin(x)))))


try:
    link = ("http://suninjuly.github.io/explicit_wait2.html")
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()

    ch1 = browser.find_element_by_id("input_value")
    x = ch1.text
    x = int(x)
    y = calc(x)
    y = ("{}".format(y))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
