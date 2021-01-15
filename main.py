from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

import time

contact = "Влад" # На Женюньчик -- ломается
text = "Hey, this message was sent using Selenium"
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
inp_xpath_search = "//*[@id=\"side\"]/div[1]/div/label/div/div[2]"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
time.sleep(2)
selected_menu = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div[@title='Меню']")\
                #/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div
                #/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[3]/div
                #//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[1]/div/img
                #//*[@id="app"]/div/span[3]/div/div/div[2]/div/div/div/div/img
selected_menu.click()
selected_menu = driver.find_element_by_xpath("//div[@title='Данные контакта']")
selected_menu.click()
selected_menu = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[1]/div/img")
selected_menu.click()
time.sleep(2)
img = driver.find_elements_by_xpath('//img')
print(img)
actionChains = ActionChains(driver)
actionChains.context_click(img[1]).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
#input_box.send_keys(text + Keys.ENTER)
time.sleep(2)
#driver.quit()