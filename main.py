import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

sno = "student number"
password = "password"
url = "http://www.cas.mcmaster.ca/~franek/courses/cs3mi3/"

s = Service("./chromedriver")
driver = webdriver.Chrome(service=s)

driver.get(url)
time.sleep(1)

login_btn_1 = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td")
login_btn_1.click()
time.sleep(1)

sno_form = driver.find_element(By.NAME, "sno")
sno_form.send_keys(sno)
time.sleep(1)

login_btn_2 = driver.find_element(By.NAME, "login")
login_btn_2.click()
time.sleep(1)

password_form = driver.find_element(By.NAME, "p1")
password_form.send_keys(password)
time.sleep(1)

login_btn_3 = driver.find_element(By.NAME, "login")
login_btn_3.click()
time.sleep(2)

# driver.quit()