from selenium import webdriver
import time
import os

print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(__file__))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Vasya")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Nikolaev")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("sxxxx@mail.ru")

    file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '12.txt')
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
