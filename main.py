from selenium import webdriver
import time

timeout = time.time() + 5
score_timeout = time.time() + 20
cookie_link = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "Y:\development\chromedriver.exe"

webdriver = webdriver.Chrome(chrome_driver_path)
webdriver.get(cookie_link)
cookie = webdriver.find_element_by_id('cookie')
money = webdriver.find_element_by_id("money")
store = webdriver.find_element_by_id("store")
print(money.text)

def buy():
    all_store_elements = store.find_elements_by_tag_name('div')
    all_store_elements.reverse()
    for element in all_store_elements:
        if not element.get_attribute('class') == 'grayed':
            element.click()
            break

while True:
    cookie.click()
    if time.time() > timeout:
        timeout = time.time() + 5
        buy()
    if time.time() > score_timeout:
        score_timeout = time.time() + 60 * 5
        cps = webdriver.find_element_by_id('cps')
        print(cps.text)

webdriver.quit()
