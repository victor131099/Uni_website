% include templates/header.tpl

<div style="margin-top:120px; padding:2%">
<h1 class = "javascript-title">Request Routing </h1>
<p>Here is the routing part of the “Hello World” example</p>
<pre>
    <code>
    @route('/hello')
    def hello():
        return "Hello World!"
    </code>
</pre>
<h2><b>Dynamic Routes¶</b></h2>
<p>
Routes that contain wildcards are called dynamic routes (as opposed to static routes) and match more than one URL at the same time. A simple wildcard consists of a name enclosed in angle brackets (e.g. <name>) and accepts one or more characters up to the next slash (/). For example, the route /hello/<name> accepts requests for /hello/alice as well as /hello/bob, but not for /hello, /hello/ or /hello/mr/smith.

Each wildcard passes the covered part of the URL as a keyword argument to the request callback. You can use them right away and implement RESTful, nice-looking and meaningful URLs with ease. Here are some other examples along with the URLs they’d match:
</p>
<pre>
    <code>
    @route('/wiki/<pagename>')            # matches /wiki/Learning_Python
    def show_wiki_page(pagename):
        ...

    @route('/<action>/<user>')            # matches /follow/defnull
    def user_api(action, user)
        ....
    </code>
</pre>
<p>
Filters can be used to define more specific wildcards, and/or transform the covered part of the URL before it is passed to the callback. A filtered wildcard is declared as <name:filter> or <name:filter:config>. The syntax for the optional config part depends on the filter used.
</p>
<p>Let’s have a look at some practical examples:</p>
<pre>
    <code>
    @route('/object/<id:int>')
    def callback(id):
        assert isinstance(id, int)

    @route('/show/<name:re:[a-z]+>')
    def callback(name):
        assert name.isalpha()

    @route('/static/<path:path>')
    def callback(path):
        return static_file(path, ...)
    </code>
</pre>
<h2><b>HTTP Request Methods</b></h2>
<p>
The HTTP protocol defines several request methods (sometimes referred to as “verbs”) for different tasks. GET is the default for all routes with no other method specified. These routes will match GET requests only. To handle other methods such as POST, PUT, DELETE or PATCH, add a method keyword argument to the route() decorator or use one of the five alternative decorators: get(), post(), put(), delete() or patch().

The POST method is commonly used for HTML form submission. This example shows how to handle a login form using POST:
</p>
<pre>
    <code>
    from bottle import get, post, request # or route

    @get('/login') # or @route('/login')
    def login():
        return '''
            &lt;form action="/login" method="post"&gt;
                Username: &lt;input name="username" type="text" /&gt;
                Password: &lt;input name="password" type="password" /&gt;
                &lt;input value="Login" type="submit" /&gt;
            &lt;/form&gt;
        '''

    @post('/login') # or @route('/login', method='POST')
    def do_login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        if check_login(username, password):
            return "&lt;p&gt;Your login information was correct.&lt;/p&gt;"
        else:
            return "&lt;p>Login failed.&lt;/p&gt;"
    </code>
</pre>

<h2><b>Routing Static Filess</b></h2>
<p>
Static files such as images or CSS files are not served automatically. You have to add a route and a callback to control which files get served and where to find them:
</p>
<pre>
    <code>
    from bottle import static_file
    @route('/static/<filename>')
    def server_static(filename):
        return static_file(filename, root='/path/to/your/static/files')
    </code>
</pre>
<p>The static_file() function is a helper to serve files in a safe and convenient way (see Static Files). This example is limited to files directly within the /path/to/your/static/files directory because the <filename> wildcard won’t match a path with a slash in it</p>
</div>
% include templates/tailer.tpl