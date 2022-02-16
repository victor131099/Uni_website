#User 2: Test successful registration process, followed by login.
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
driver = Firefox(options=opts)
baseURL = 'https://10.86.225.18'
driver.get(baseURL)

#first create a random Username (e.g. testUser1A245ZAG95IQ)

test_username = "testUser_".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
test_firstname = test_username
test_lastname = "test"
test_email = test_username + "@uni.sydney.edu.au"
test_password = "password"

max_delay = 3 # seconds
try:
    signup_button = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/p/a[1]')))
    signup_button.click()
    reached_signup = False
    if(driver.current_url == (baseURL + "/signup")):
        reached_signup = True
    print("successfully reached signup page: " + str(reached_signup))
except TimeoutException:
    print ("Loading page took too long.")

email_field = driver.find_element_by_xpath("/html/body/div/div/form/input[1]")
email_field.send_keys(test_email)

firstname_field = driver.find_element_by_xpath("/html/body/div/div/form/input[2]")
firstname_field.send_keys(test_firstname)

lastname_field = driver.find_element_by_xpath("/html/body/div/div/form/input[3]")
lastname_field.send_keys(test_lastname)

username_field = driver.find_element_by_xpath("/html/body/div/div/form/input[4]")
username_field.send_keys(test_username)

password_field = driver.find_element_by_xpath("/html/body/div/div/form/input[5]")
password_field.send_keys(test_password)

#submit and login
try:
    submit_signup_button = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[6]')))
    submit_signup_button.click()
    reached_signup = False
    if(driver.current_url == (baseURL + "/signup")):
        reached_signup = True
    print("successfully signed up: " + str(reached_signup))
except TimeoutException:
    print ("Loading page took too long.")


#Logout
try:
    Logout_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[8]')))
    Logout_header_link.click()
    print("successful logout, " + driver.current_url)
except TimeoutException:
    print ("Loading page took too long.")

driver.close()
quit()
