#User 7: Test Admin functionality: Remove user

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
member_count = 0

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

#add user
test_username = "testUser_".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
test_firstname = test_username
test_lastname = "test"
test_email = test_username + "@uni.sydney.edu.au"
test_password = "password"

member_count = (len(driver.find_elements_by_xpath('/html/body/div[3]/div[2]/article/table/tbody/tr')) - 1) #exclude title row
print("initial user count: " + str(member_count))

try:
    adduser_firstname = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/article/div/form/input[2]')))
    adduser_firstname.send_keys(test_firstname)

    adduser_lastname = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/article/div/form/input[3]')))
    adduser_lastname.send_keys(test_lastname)

    adduser_email = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/article/div/form/input[4]')))
    adduser_email.send_keys(test_email)

    adduser_username = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/article/div/form/input[5]')))
    adduser_username.send_keys(test_username)

    adduser_password = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/article/div/form/input[6]')))
    adduser_password.send_keys(test_password)

    adduser_submit = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/article/div/form/input[7]')))
    adduser_submit.click()
except TimeoutException:
    print ("Loading page took too long.")

time.sleep(1)
member_count = (len(driver.find_elements_by_xpath('/html/body/div[3]/div[2]/article/table/tbody/tr')) - 1) #exclude title row
print("user: " + test_username + "successfully added, user count: " + str(member_count))

#now remove the new user
try:
    Remove_button = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/article/table/tbody/tr[{member}]/td/form/input[3]'.format(member = str(member_count + 1)))))
    Remove_button.click()
except TimeoutException:
    print ("Loading page took too long.")

time.sleep(1)
member_removed = (len(driver.find_elements_by_xpath('/html/body/div[3]/div[2]/article/table/tbody/tr')) - 1) #exclude title row
print("User successfully removed: new user count = " + str(member_removed))


#Logout
try:
    Logout_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[9]')))
    Logout_header_link.click()
    print("successful logout, " + driver.current_url)
except TimeoutException:
    print ("Loading page took too long.")

driver.close()
quit()
