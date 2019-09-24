from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    ch1 = browser.find_element_by_id("num1")
    ch1 = ch1.text
    ch2 = browser.find_element_by_id("num2")
    ch2 = ch2.text
    summa = int(ch1) + int(ch2)
    summa = "{}".format(summa)


    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(summa)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
