#User 5: Test User forum functionality including: search posts, create post and reply to post.
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time

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
current_number_of_forum_questions = 0
current_number_of_question_responses = ""

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

#search forum
try:
    Forum_search_field = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/form/input[1]')))
    Forum_search_field.send_keys("<p>")
    #count number of questions : used to determine if we can successfully create a post later
    current_number_of_forum_questions = (len(driver.find_elements_by_xpath('/html/body/div/table/tbody/tr')) - 1) #exclude title row
    print("Current forum questions: " + str(current_number_of_forum_questions))

    Forum_search_submit = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/form/input[2]')))
    Forum_search_submit.click()

    reached_forum_question = False
    if(driver.current_url == (baseURL + "/forum?question=%3Cp%3E")):
        reached_forum_question = True
    print("successfully searched for question '<p>': " + str(reached_forum_question))
except TimeoutException:
    print ("Loading page took too long.")

#go to post page
try:
    Forum_create_post = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/form/input')))
    Forum_create_post.click()
    reached_forum_post = False
    if(driver.current_url == (baseURL + "/post?")):
        reached_forum_post = True
    print("successfully reached post page: " + str(reached_forum_post))
except TimeoutException:
    print ("Loading page took too long.")

#post question
try:
    Forum_post_title = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[1]')))
    Forum_post_title.send_keys("testQuestion_".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)))

    Forum_post_body = driver.find_element_by_xpath('/html/body/div/div/form/textarea')
    Forum_post_body.send_keys("testQuestionBody_".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)))

    Forum_post_submit = driver.find_element_by_xpath("/html/body/div/div/form/input[2]")
    Forum_post_submit.click()

    #count number of questions in forum
    title = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/table/tbody/tr[2]/th/a')))
    if((len(driver.find_elements_by_xpath('/html/body/div/table/tbody/tr')) - 1) == (current_number_of_forum_questions)):
        print("Forum question successfully added: new forum count = " + str(current_number_of_forum_questions + 1))
except TimeoutException:
    print ("Loading page took too long.")

#view question and reply
try:
    Forum_question_link = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/table/tbody/tr[2]/th/a")))
    Forum_question_link.click()

    Forum_question_reply_field = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/ul/form/input[1]")))
    Forum_question_reply_field.send_keys("testReply_".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)))

    current_number_of_question_responses = driver.find_element_by_xpath('/html/body/div/div/ul/h1').text

    Forum_question_reply_button = driver.find_element_by_xpath('/html/body/div/div/ul/form/input[2]')
    Forum_question_reply_button.click()

    try:
        num = current_number_of_question_responses.split()
        curr_num = (int(num[0]) + 1)
        expected_questions = (str(curr_num) + " responses")
        print("test question has: " + expected_questions)

        time.sleep(2)
        new_responses = WebDriverWait(driver, max_delay).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/ul/h1"), expected_questions))
        new_responses_text = driver.find_element_by_xpath('/html/body/div/div/ul/h1').text
        print("posted new response: previously " + current_number_of_question_responses + ", now there are: "+ new_responses_text)

    except TimeoutException:
        print ("Loading page took too long.")

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
