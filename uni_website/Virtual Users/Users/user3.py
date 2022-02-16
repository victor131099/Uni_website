#User 3: Test unsuccessful login process.

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
login_name.send_keys('fakeAccount')
login_password = driver.find_element_by_xpath("/html/body/div/div/form/input[2]")
login_password.send_keys('incorrectPassword')


max_delay = 3 # seconds
try:
    login_form = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[3]')))
    login_form.click()
    reached_home = False
    if(driver.current_url == (baseURL + "/login")):
        reached_home = True
    print("Unable to log in with a fake user: " + str(reached_home))
    if(reached_home == True):
        print("Test Successful.")
except TimeoutException:
    print ("Loading page took too long.")


driver.close()
quit()
