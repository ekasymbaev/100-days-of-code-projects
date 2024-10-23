from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/HP-24mh-FHD-Monitor-Built/dp/B08BF4CZSV/ref=sr_1_14?crid=22S5HJ7OPFNPF&dib=eyJ2IjoiMSJ9.eFQfRY192i5VDLaTvEZLksnp0Q2xpJ4EgtrRQOOZVds3ViIg5i7uHxoO1eyDYKr-VH2pK1TuUHzTuDPR6EPif4dbiJYzeynKr9-MffArFetEb3FRaB5oQJBhjq-eeDcCcs68GBY6XdBOomOMZrpqL9pldrF7QUXdcE4_bHRZNbOFj0Ie7fN2KdNIC28AwEDfymFtv2Tp_l2QQW2mxs7v7gfojjr_2bHkRcSvUIMaA6A.1uurX6_Scx9ReQ6M6eNJe5FCZ1WoYdpeTec3ZakPu5w&dib_tag=se&keywords=monitors&qid=1729653421&sprefix=monitors%2Caps%2C120&sr=8-14")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}. {price_cents.text}")


driver.quit()