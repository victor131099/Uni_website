#User 1: Test user login, content page navigation, and logout functionality.
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
driver = Firefox(options=opts)
baseURL = 'https://10.86.225.18'
driver.get(baseURL)

#Login
#login_name = driver.find_element_by_name('username')
login_name = driver.find_element_by_xpath("/html/body/div/div/form/input[1]")
login_name.send_keys('Tom')
login_password = driver.find_element_by_xpath("/html/body/div/div/form/input[2]")
login_password.send_keys('Tom')
login_form = driver.find_element_by_xpath("/html/body/div/div/form/input[3]")
login_form.click()

#made it to the home page
print("successful login: current page = " + driver.current_url)

#now load each content page
#Html content
max_delay = 3 # seconds
try:
    html_content_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[2]')))
    html_content_header_link.click()
    reached_html = False
    if(driver.current_url == (baseURL + "/html_content")):
        reached_html = True
    print("successfully reached html page: " + str(reached_html))
except TimeoutException:
    print ("Loading page took too long.")

#CSS content
try:
    css_content_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[3]')))
    css_content_header_link.click()
    reached_css = False
    if(driver.current_url == (baseURL + "/css")):
        reached_css = True
    print("successfully reached css page: " + str(reached_css))
except TimeoutException:
    print ("Loading page took too long.")

#Javascript content
try:
    Javascript_content_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[4]')))
    Javascript_content_header_link.click()
    reached_javascript = False
    if(driver.current_url == (baseURL + "/javascript")):
        reached_javascript = True
    print("successfully reached javascript page: " + str(reached_javascript))
except TimeoutException:
    print ("Loading page took too long.")

#Frameworks content
try:
    Frameworks_content_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[5]')))
    Frameworks_content_header_link.click()
    reached_frameworks = False
    if(driver.current_url == (baseURL + "/frameworks")):
        reached_frameworks = True
    print("successfully reached frameworks page: " + str(reached_frameworks))
except TimeoutException:
    print ("Loading page took too long.")

#Bottle content
try:
    Bottle_content_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[6]')))
    Bottle_content_header_link.click()
    reached_bottle = False
    if(driver.current_url == (baseURL + "/bottle")):
        reached_bottle = True
    print("successfully reached bottle page: " + str(reached_bottle))
except TimeoutException:
    print ("Loading page took too long.")

#Forum
try:
    Forum_header_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/a[7]')))
    Forum_header_link.click()
    reached_forum = False
    if(driver.current_url == (baseURL + "/forum")):
        reached_forum = True
    print("successfully reached forum page: " + str(reached_forum))
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
