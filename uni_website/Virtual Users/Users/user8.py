#User 8: Test Admin functionality: Mute and unmute user

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
driver = Firefox(options=opts)
baseURL = 'https://10.86.225.18'
driver.get(baseURL)

#Login with admin account
login_name = driver.find_element_by_xpath("/html/body/div/div/form/input[1]")
login_name.send_keys('Tom')
login_password = driver.find_element_by_xpath("/html/body/div/div/form/input[2]")
login_password.send_keys('tom')
login_form = driver.find_element_by_xpath("/html/body/div/div/form/input[3]")
login_form.click()


#made it to the home page
print("successful admin login: current page = " + driver.current_url)

#load admin page
max_delay = 3 # seconds
try:
    admin_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[8]')))
    admin_header_link.click()
    reached_admin_page = False
    if(driver.current_url == (baseURL + "/admin")):
        reached_admin_page = True
    print("successfully reached admin page: " + str(reached_admin_page))
    print("successfully reached admin page: " + driver.current_url)
except TimeoutException:
    print ("Loading page took too long.")

time.sleep(1)

try:
    user_mute_status = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article/table/tbody/tr[2]/td[1]').text
    print("initial mute status: " + user_mute_status)
    mute_user_toggle = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/article/table/tbody/tr[2]/td[2]/form/input[4]')))
    mute_user_toggle.click()
except TimeoutException:
    print ("Loading page took too long.")

time.sleep(1)
try:
    user_mute_status = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article/table/tbody/tr[2]/td[1]').text
    print("updated mute status: " + user_mute_status)
    mute_user_toggle = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/article/table/tbody/tr[2]/td[2]/form/input[4]')))
    mute_user_toggle.click()
except TimeoutException:
    print ("Loading page took too long.")

time.sleep(1)
try:
    user_mute_status = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article/table/tbody/tr[2]/td[1]').text
    print("reverted mute status: " + user_mute_status)
except TimeoutException:
    print ("Loading page took too long.")

#Logout
try:
    Logout_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[9]')))
    Logout_header_link.click()
    print("successful logout, " + driver.current_url)
except TimeoutException:
    print ("Loading page took too long.")

driver.close()
quit()
