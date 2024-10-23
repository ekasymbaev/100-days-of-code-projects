from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org")

# number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")

#closing driver
answer = input("do you want to close?")
if answer.lower() == "yes":

    driver.quit()