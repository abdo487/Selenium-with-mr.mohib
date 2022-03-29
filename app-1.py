from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
p = driver.get("http://aviation.meteo.fr/")

name = driver.find_element_by_name("login")
name.clear()
name.send_keys("Mohibyoussef")

pwd = driver.find_element_by_name("password")
pwd.clear()
pwd.send_keys("mohibyousseF0")

valid = driver.find_element_by_css_selector("input[type='submit']")
valid.click()

# a.send_keys(Keys.RETURN)
