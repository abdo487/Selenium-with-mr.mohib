from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
p = driver.get("http://aviation.meteo.fr/")


# L euthentication dans le site
name = driver.find_element(By.NAME, value="login")
name.clear()
name.send_keys("Mohibyoussef")

sleep(2)
pwd = driver.find_element(By.NAME, value="password")
pwd.clear()
pwd.send_keys("mohibyousseF0")

valid = driver.find_element(By.CSS_SELECTOR, value="input[type='submit']")
valid.click()

sleep(5)
item = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[3]/span[2]/a")
item.click()

sleep(5)
field = driver.find_element(By.NAME, value="aero3")
field.clear()
field.send_keys("GMMX")

sleep(2)
confirmSubmit = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody/tr[2]/td/img")
confirmSubmit.click()

sleep(10)
driver.quit()