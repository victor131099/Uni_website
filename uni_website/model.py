'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view
import random
import sql
from hashlib import sha256
import jwt
import json
from bottle import template, request, response
from datetime import datetime
import time


# Initialise our views, all arguments are defaults for the template
page_view = view.View()
db = sql.SQLDatabase()
key = "retract,bran,scupper,ameba"
cookie_timeout = 45*60  # cookies expire after 45 mins
# -----------------------------------------------------------------------------
# post
# -----------------------------------------------------------------------------


def post():
    '''
        post
        Returns the post view
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/post", isMuted=db.check_user_muted(cookie), isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)


def post_quesiton():
    cookie = get_cookie()
    if not cookie:
        err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
        return template("templates/invalid", reason=err_str, isAdmin=False)

    title = request.forms.get('title')
    description = request.forms.get('description')
    db.create_post(title, description, cookie)
    return True

# -----------------------------------------------------------------------------
# javascript
# -----------------------------------------------------------------------------


def javascript():
    '''
        javascript
        Returns the javascript view
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/javascript", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)

# -----------------------------------------------------------------------------
# javascript page
# -----------------------------------------------------------------------------


def javascriptButton():
    '''
        {page}
        Returns the {page} view
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/javascriptButton", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)


def javascriptInput():
    '''
        {page}
        Returns the {page} view
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/javascriptInput", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)


def javascriptSyntax():
    '''
        {page}
        Returns the {page} view
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/javascriptSyntax", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)


def javascriptText():
    '''
        {page}
        Returns the {page} view
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/javascriptText", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)
# -----------------------------------------------------------------------------
# forum
# -----------------------------------------------------------------------------


def forum():
    '''
        forum
        :: rows :: The rows
        Returns the forum view
    '''
    cookie = get_cookie()
    if not cookie:
        err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
        return template("templates/invalid", reason=err_str, isAdmin=False)

    word = request.query.question
    print(word)
    if word == "":
        result = db.display_questions()
    else:
        result = db.search_question(word)
    return template("templates/forum.tpl", rows=result, isMuted=db.check_user_muted(cookie), isAdmin=db.is_admin(cookie))


# -----------------------------------------------------------------------------
# question
# -----------------------------------------------------------------------------
def question(question_id):
    '''
        question
        Display question_id

        :: question_id :: The question id

        Returns the question view
    '''
    cookie = get_cookie()
    if not cookie:
        err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
        return template("templates/invalid", reason=err_str, isAdmin=False)
    question_info = db.display_post(question_id)
    now = datetime.now()
    date_time_obj = datetime.strptime(question_info[2], '%Y-%m-%d %H:%M:%S')
    subtract = now - date_time_obj
    time = days_hours_minutes(subtract)
    time_str = ""
    if time[0] == 0:
        if(time[1] == 0):
            time_str = str(time[2]) + " mins ago"
        else:
            time_str = str(time[1]) + " hours ago"
    else:
        time_str = str(time[0]) + " days ago"
    print("comment")
    result = db.display_comment(question_id)

    return template("templates/question.tpl",
                    question_info=question_info, time_str=time_str, comments=result, isMuted=db.check_user_muted(cookie), isAdmin=db.is_admin(cookie))


def days_hours_minutes(td):
    return (td.days, td.seconds//3600, (td.seconds//60) % 60)


def post_comment(qid):
    comment = request.forms.get('comment')
    cookie = get_cookie()
    db.comment_post(comment, qid, cookie)
    return True
# -----------------------------------------------------------------------------
# index
# -----------------------------------------------------------------------------


def index():
    '''
        index
        Returns the view for the index
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/index", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)

# -----------------------------------------------------------------------------
# Login
# -----------------------------------------------------------------------------


def bottle():
    '''
        index
        Returns the view for bottle page
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/bottle", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)


def request_data():
    '''
        index
        Returns the view for the index
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/request_data", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)


def request_route():
    '''
        index
        Returns the view for the index
    '''
    cookie = get_cookie()
    return template("templates/request_route", isAdmin=db.is_admin(cookie))


def request_template():
    '''
        index
        Returns the view for the index
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/request_template", isAdmin=db.is_admin(cookie))

    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
    return template("templates/invalid", reason=err_str, isAdmin=False)


def login_form():
    '''
        login_form
        Returns the view for the login_form
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/index", isAdmin=db.is_admin(cookie))
    return template("templates/login")


def log_out():
    '''
        Log user out of the website
        Returns login form
    '''
    response.delete_cookie("token")
    return template("templates/login")
# -----------------------------------------------------------------------------

# Check the login credentials


def login_check(username, password):
    '''
        login_check
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    '''
    ip = request.environ.get('REMOTE_ADDR')
    timestamp = time.time()
    curr_id = str(db.get_userid(username))
    err_str = "Password or username is incorrect. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
    if not db.login_allowed(curr_id):
        err_str = "This account is now locked. Try again later."
    elif db.check_credentials(username, password):
        json = {
            "id": curr_id,
            "username": username,
            "ip": ip,
            "timestamp": timestamp,
        }
        token = jwt.encode(json, key, algorithm="HS256")
        # hashed_id = sha256(curr_id.encode()).hexdigest()
        response.set_header("SET-COOKIE", "token=" +
                            token + "; HttpOnly; SameSite=Strict; Secure")
        db.add_login_attempt(curr_id, True)
        return template("templates/index", name=username, isAdmin=db.is_admin(curr_id))

    db.add_login_attempt(curr_id, False)
    return template("templates/invalid", reason=err_str, isAdmin=False)


def get_cookie():
    user_cookie = request.get_cookie("token")
    try:
        decoded_jwt = jwt.decode(user_cookie, key, algorithms=["HS256"])
    except jwt.exceptions.DecodeError:
        return False
    json_id = decoded_jwt["id"]
    json_username = decoded_jwt["username"]
    json_ip = decoded_jwt["ip"]
    json_timestamp = decoded_jwt["timestamp"]
    id_result = db.check_id_username(json_id, json_username)
    if id_result and json_ip == request.environ.get('REMOTE_ADDR') and time.time() <= json_timestamp+cookie_timeout:
        return id_result
    return False

# -----------------------------------------------------------------------------
# Signup
# -----------------------------------------------------------------------------


def add_user(username, password):
    if not db.user_exists(username):
        db.add_user(username, password, 0)
        return template("templates/login")

    return template("templates/invalid", reason="Sorry, that username already exists.<br><br><a class='button' href='/signup'>Try Again</a>", isAdmin=False)


def signup_form():
    '''
        signup_form
        Returns the view for the signup_form
    '''
    return template("templates/signup")


# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# About
# -----------------------------------------------------------------------------


def about():
    '''
        about
        Returns the view for the about page
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/about", garble=about_garble(), isAdmin=db.is_admin(cookie))

    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
    return template("templates/invalid", reason=err_str, isAdmin=False)


# Returns a random string each time
def about_garble():
    '''
        about_garble
        Returns one of several strings for the about page
    '''
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
              "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
              "organically grow the holistic world view of disruptive innovation via workplace change management and empowerment.",
              "bring to the table win-win survival strategies to ensure proactive and progressive competitive domination.",
              "ensure the end of the day advancement, a new normal that has evolved from epistemic management approaches and is on the runway towards a streamlined cloud solution.",
              "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]

# -----------------------------------------------------------------------------
# HTML Content
# -----------------------------------------------------------------------------


def html_content():
    '''
        html_content
        Returns the view for the html_content
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/html_content", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)

# -----------------------------------------------------------------------------
# CSS Content
# -----------------------------------------------------------------------------


def css_content():
    '''
        css_content
        Returns the view for the css content
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/css", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"

    return template("templates/invalid", reason=err_str, isAdmin=False)

# -----------------------------------------------------------------------------
# Webframeworks Content
# -----------------------------------------------------------------------------


def frameworks():
    '''
        frameworks
        Returns the view for the Web Frameworks content
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/frameworks", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
    return template("templates/invalid", reason=err_str, isAdmin=False)


# -----------------------------------------------------------------------------
# Admin panel
# -----------------------------------------------------------------------------
# Admin page
def admin():
    '''
        admin
        Returns the view for the admin page
    '''
    results = db.get_all_users_muted()
    cookie = get_cookie()
    if cookie:
        if db.is_admin(cookie):
            return template("templates/admin", rows=results, isAdmin=db.is_admin(cookie))
        err_str = "Not an admin"
        return template("templates/invalid", reason=err_str, isAdmin=False)
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
    return template("templates/invalid", reason=err_str, isAdmin=False)

# Admin add user via admin panel


def admin_add_user(username, password):
    '''
        admin_add_user
        Add new user via admin panel
    '''
    cookie = get_cookie()

    if len(username) == 0:
        return template("templates/invalid", reason="Please enter a username<br><br><a class='button' href='/admin'>Try Again</a>", isAdmin=db.is_admin(cookie))

    if len(password) == 0:
        return template("templates/invalid", reason="Please enter a password<br><br><a class='button' href='/admin'>Try Again</a>", isAdmin=db.is_admin(cookie))

    if not db.user_exists(username):
        db.add_user(username, password, 0)
        db.get_all_users()
        return admin()
    return template("templates/invalid", reason="Sorry, that username already exists.<br><br><a class='button' href='/admin'>Try Again</a>", isAdmin=db.is_admin(cookie))

# Admin remove user via admin panel


def admin_del_user(username):
    '''
        admin_del_user
        Remove user via admin panel
    '''
    cookie = get_cookie()
    if not db.user_exists(username):
        return template("templates/invalid", reason="Cannot remove user, that username does not exist.<br><br><a class='button' href='/admin'>Try Again</a>", isAdmin=db.is_admin(cookie))

    db.delete_user(username)
    return admin()

# Admin mute user via admin panel


def admin_mute_user(username, isMuted):
    '''
        admin_mute_user
        Mute or unmute user via admin panel
    '''
    cookie = get_cookie()
    if not db.user_exists(username):
        return template("templates/invalid", reason="Cannot remove user, that username does not exist.<br><br><a class='button' href='/admin'>Try Again</a>", isAdmin=db.is_admin(cookie))

    db.mute_user(username, isMuted)
    return admin()

# -----------------------------------------------------------------------------
# Debug
# -----------------------------------------------------------------------------


def debug(cmd):
    try:
        return str(eval(cmd))
    except:
        pass


# -----------------------------------------------------------------------------
# 404
# Custom 404 error page
# -----------------------------------------------------------------------------

def handle_errors(error):
    error_type = error.status_line
    error_msg = error.body

    cookie = get_cookie()
    if not cookie:
        return template("templates/error", error_type=error_type, error_msg=error_msg, isAdmin=cookie)
    return template("templates/error", error_type=error_type, error_msg=error_msg, isAdmin=db.is_admin(cookie))


# css page
# -----------------------------------------------------------------------------

def css():
    '''
        css
        Returns the css view
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/css", isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
    return template("templates/invalid", reason=err_str, isAdmin=False)


# css page
# -----------------------------------------------------------------------------

def csspage(page):
    '''
        {page}
        Returns the {page} view
    '''
    cookie = get_cookie()
    if cookie:
        return template("templates/" + page, isAdmin=db.is_admin(cookie))
    err_str = "Not logged in. Please <a href='/login'>try again</a>, or create a new account.<br><br><a class='button' href='/login'>Try Again</a>"
    return template("templates/invalid", reason=err_str, isAdmin=False)
# -----------------------------------------------------------------------------
