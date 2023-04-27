import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the websit

driver.get('https://pubs.acs.org/action/ssostart?idp=https%3A%2F%2Fshibboleth.umontreal.ca%2Fidp%2Fshibboleth&redirectUri=%2Fpage%2Fremoteaccess%2Fconfirm&federationId=https%3A%2F%2Fcaf-fcga.ca%2Fentity')
driver.implicitly_wait(5)
time.sleep(10)
Pnumber = driver.find_element(By.ID, 'username')
Password = driver.find_element(By.ID, 'password')

Pnumber.send_keys('StudentID')
Password.send_keys('********')

driver.implicitly_wait(5)
time.sleep(10)
content = driver.find_element(By.CSS_SELECTOR, 'button.form-element.form-button')
content.click()

# Find login button
#login_button = driver.find_element(By.ID, 'Buttons')
#content = driver.find_element(By.CSS_SELECTOR, 'a.yt-spec-button-shape-next.yt-spec-button-shape-next--outline.yt-spec-button-shape-next--call-to-action.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-leading')
driver.implicitly_wait(20)
time.sleep(10)
driver.get('https://pubs.acs.org/doi/10.1021/acs.jmedchem.2c00857')
driver.implicitly_wait(30)
time.sleep(10)
content = driver.find_element(By.ID, 'prevID')
content.click()
driver.implicitly_wait(30)
time.sleep(10)
content = driver.find_element(By.ID, 'prevID')
