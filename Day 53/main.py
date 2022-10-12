from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import requests

URL = "https://stackoverflow.com/questions/51925384/unable-to-get-local-issuer-certificate-when-using-requests-in-python"

page = requests.get(URL)
print(page.text)

# driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
#
# driver.get(URL)
# driver.implicitly_wait(1)
#
# kb_listing = {"Name": [], "Price": [], "Sale Type": []}

# GRABS THE KB NAMES
# kb_names_elem = driver.find_elements(By.XPATH, '//h1[@class="sc-fznWOq cqDPIl"]')
# for n in kb_names_elem:
#     kb_listing["Name"].append(n.text)

# GRABS THE KB PRICES
# kb_prices_elem = driver.find_elements(By.XPATH, '//span[@class="sc-fznzOf jxQFAb"]')
# x = 0
# for n in kb_prices_elem:
#     x += 1
#     if x % 4 == 3:
#         kb_listing["Price"].append(n.text.strip("()USD"))

# GRABS THE SALE TYPE
# kb_prices_elem = driver.find_elements(By.XPATH, '//span[@class="sc-fznzOf jxQFAb"]')
# x = 0
# for n in kb_prices_elem:
#     x += 1
#     if x % 4 == 0:
#         kb_listing["Sale Type"].append(n.text)

# print(kb_listing)
# driver.quit()
