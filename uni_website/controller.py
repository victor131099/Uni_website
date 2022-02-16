'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''

from bottle import route, get, post, error, request, static_file, redirect, template, Bottle, run
import model
import html
qid = 1

app = application = Bottle()
isProduction = False

# -----------------------------------------------------------------------------
# Static file paths
# -----------------------------------------------------------------------------

# Allow image loading


@app.route('/img/<picture:path>')
def serve_pictures(picture):
    '''
        serve_pictures

        Serves images from static/img/

        :: picture :: A path to the requested picture

        Returns a static file object containing the requested picture
    '''
    return static_file(picture, root='static/img/')

# -----------------------------------------------------------------------------

# Allow CSS


@app.route('/css/<css:path>')
def serve_css(css):
    '''
        serve_css

        Serves css from static/css/

        :: css :: A path to the requested css

        Returns a static file object containing the requested css
    '''
    return static_file(css, root='static/css/')

# -----------------------------------------------------------------------------

# Allow javascript


@app.route('/js/<js:path>')
def serve_js(js):
    '''
        serve_js

        Serves js from static/js/

        :: js :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(js, root='static/js/')

# -----------------------------------------------------------------------------
# Pages
# -----------------------------------------------------------------------------

# Redirect to login


@app.get('/home')
def get_index():
    '''
        get_index

        Serves the index page
    '''
    return model.index()

# -----------------------------------------------------------------------------

# Display the Discussion page


@app.get('/forum')
def get_forum():
    '''
        get_forum

        Serves the forum page
    '''
    return model.forum()

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

# Display the create post page


@app.get('/post')
def get_post():
    '''
        get_post

        Serves the post page
    '''
    return model.post()


@app.post('/post')
def post_post():
    model.post_quesiton()
    redirect("/forum")

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

# Display the javascript page


@app.get('/javascript')
def get_javascript():
    '''
        get_javascript

        Serves the javascript page
    '''
    return model.javascript()


# -----------------------------------------------------------------------------

# Display the javascript subpage
@app.get('/javascriptButton')
def get_javascriptButton():
    '''
        get_javascript

        Serves the javascript page
    '''

    return model.javascriptButton()


@app.get('/javascriptInput')
def get_javascriptInput():
    '''
        get_javascript

        Serves the javascript page
    '''

    return model.javascriptInput()


@app.get('/javascriptText')
def get_javascriptText():
    '''
        get_javascript

        Serves the javascript page
    '''

    return model.javascriptButton()


@app.get('/javascriptSyntax')
def get_javascriptSyntax():
    '''
        get_javascript

        Serves the javascript page
    '''

    return model.javascriptSyntax()


@app.get('/javascriptInput')
def get_javascriptInput():
    '''
        get_javascript

        Serves the javascript page
    '''

    return model.javascriptInput()


@app.get('/javascriptText')
def get_javascriptText():
    '''
        get_javascript

        Serves the javascript page
    '''

    return model.javascriptText()
# -----------------------------------------------------------------------------

# Display the question page


@app.get('/question')
def get_forum():
    '''
        get_question

        Serves the question page
    '''
    question_id = int(request.query.id)
    global qid
    qid = question_id
    return model.question(question_id)


@app.post('/comment')
def post_comments():
    model.post_comment(qid)
    return redirect('/question?id=' + str(qid))


@app.post('/search')
def search_question():
    word = html.escape(request.forms.get('search'))
    return redirect('/forum?question=' + word)

# Display the login page


@app.get('/')
@app.get('/login')
def get_login_controller():
    '''
        get_login

        Serves the login page
    '''
    return model.login_form()

# -----------------------------------------------------------------------------

# Attempt the login


@app.post('/login')
def post_login():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = html.escape(request.forms.get('username'))
    password = html.escape(request.forms.get('password'))

    # Call the appropriate method
    return model.login_check(username, password)


# -----------------------------------------------------------------------------


# Display the signup page
@app.get('/signup')
def get_signup_controller():
    '''
        get_signup

        Serves the login page
    '''
    return template("templates/signup")

# -----------------------------------------------------------------------------

# Attempt the signup


@app.post('/signup')
def post_signup():
    '''
        post_signup

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = html.escape(request.forms.get('username'))
    password = html.escape(request.forms.get('password'))

    # Call the appropriate method
    return model.add_user(username, password)


# -----------------------------------------------------------------------------
@app.get('/bottle')
def get_bottle():
    '''
        get_about

        Serves the about page
    '''
    return model.bottle()


@app.get('/request_route')
def get_route():
    '''
        get_about

        Serves the about page
    '''
    return model.request_route()


@app.get('/request_data')
def get_data():
    '''
        get_about

        Serves the about page
    '''
    return model.request_route()


@app.get('/request_template')
def get_template():
    '''
        get_about

        Serves the about page
    '''
    return model.request_template()


@app.get('/about')
def get_about():
    '''
        get_about

        Serves the about page
    '''
    return model.about()
# -----------------------------------------------------------------------------


# Display the HTML content page
@app.get('/html_content')
def get_html_content():
    '''
        get_html_content

        Serves the HTML content page
    '''
    return model.html_content()

# -----------------------------------------------------------------------------

# Display the CSS content page


@app.get('/css')
def get_css_content():
    '''
        get_css_content

        Serves the HTML content page
    '''
    return model.css_content()

# -----------------------------------------------------------------------------

# Admin panel


@app.get('/admin')
def get_admin_page():
    '''
        get_admin_page

        Serves the admin page
    '''
    return model.admin()


@app.post('/admin')
def admin_controls():
    '''
        admin_controls

        1) Adds user from the admin panel
        2) Delete user from the admin panel
        3) Mute or unmute users from the admin panel.
    '''
    if(html.escape(request.forms.get('requestType')) == 'add'):
        fname = html.escape(request.forms.get('fname'))
        lname = html.escape(request.forms.get('lname'))
        email = html.escape(request.forms.get('email'))
        username = html.escape(request.forms.get('username'))
        password = html.escape(request.forms.get('password'))
        return model.admin_add_user(username, password)

    elif(html.escape(request.forms.get('requestType')) == 'remove'):
        username = html.escape(request.forms.get('username'))
        return model.admin_del_user(username)

    else:
        username = html.escape(request.forms.get('username'))
        isMuted = html.escape(request.forms.get('isMuted'))
        return model.admin_mute_user(username, isMuted)

# -----------------------------------------------------------------------------


# Help with debugging


@post('/debug/<cmd:path>')
def post_debug(cmd):
    return model.debug(cmd)

# -----------------------------------------------------------------------------

# 404 errors, use the same trick for other types of errors


@app.error(404)
def error(error):
    return model.handle_errors(error)
# -----------------------------------------------------------------------------

# Web Application Frameworks


@app.get('/frameworks')
def get_frameworks():
    '''
        get_frameworks

        Serve the web application frameworks page
    '''
    return model.frameworks()
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------

# Display the css page
@app.get('/css')
def get_css():
    '''
        get_css
        Serves the css page
    '''
    return model.css()

# -----------------------------------------------------------------------------

# Display the css subpage


@app.get('/css/<page>')
def get_css(page):
    print(page)
    '''
        get_css
        Serves the css page
    '''
    return model.csspage(page)
# -----------------------------------------------------------------------------

# Log out


@app.get('/logout')
def log_out():
    '''
        log_out
        Logs the current user off the website
    '''
    # redirect("/")
    return model.log_out()


if isProduction == False:
    print("******* APP RUNNING IN DEVELOPMENT MODE *******")
    run(app, host='localhost', port=8080)
