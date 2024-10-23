from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

name_placeholder = driver.find_element(By.NAME, value="fName")
lname_placeholder = driver.find_element(By.NAME, value="lName")
email_placeholder = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-block')


name_placeholder.send_keys("Erzhigit")
lname_placeholder.send_keys("Kasymbaev")
email_placeholder.send_keys("random@gmail.com")
button.click()

