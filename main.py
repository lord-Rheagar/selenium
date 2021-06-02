from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

PATH=r"C:\Users\Shekhar\chromedriver.exe"

driver= webdriver.Chrome(PATH)

driver.get(r"https://www.linkedin.com/")

time.sleep(4)

username=driver.find_element_by_xpath("//input[@name='session_key']")
password=driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys("bodhiswattwac@gmail.com")
password.send_keys("xyjkhkkdh")

time.sleep(2)

submit=driver.find_element_by_xpath("//button[@type='submit']").click()


time.sleep(5)

driver.get(r"https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&page=2")
time.sleep(4)

all_buttons=driver.find_elements_by_tag_name("button")
connect_buttons=[btn for btn in all_buttons if btn.text== "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(4)

    send=driver.find_element_by_xpath("//button[@aria-label= 'Send now']")
    driver.execute_script("arguments[0].click();", send)
    time.sleep(3)


