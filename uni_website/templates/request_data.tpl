% include templates/header.tpl

<div style="margin-top:120px; padding:2%">
<h1 class = "javascript-title">Request Data </h1>
<h2><b>HTML Form Handling</b></h2>
<p>Let us start from the beginning. In HTML, a typical <form> looks something like this:</p>
<pre>
    <code>
    &lt;form action="/login" method="post"&gt;
        Username: <input name="username" type="text" /&gt;
        Password: <input name="password" type="password" /&gt;
        <input value="Login" type="submit" />
    &lt;/form &gt;
    &lt;/code &gt;
</pre>
<p>The action attribute specifies the URL that will receive the form data. method defines the HTTP method to use (GET or POST). With method="get" the form values are appended to the URL and available through BaseRequest.query as described above. This is considered insecure and has other limitations, so we use method="post" here. If in doubt, use POST forms.

Form fields transmitted via POST are stored in BaseRequest.forms as a FormsDict. The server side code may look like this:</p>
<pre>
    <code>
    from bottle import route, request

    @route('/login')
    def login():
        return '''
            &lt;form action="/login" method="post"&gt;
                Username: &lt;input name="username" type="text" /&gt;
                Password: &lt;input name="password" type="password" /&gt;
                &lt;input value="Login" type="submit" /&gt;
            &lt;/form>
        '''

    @route('/login', method='POST')
    def do_login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        if check_login(username, password):
            return "&lt;p>Your login information was correct.&lt;/p&gt;"
        else:
            return "&lt;p>Login failed.&lt;/p&gt;"
    </code>
</pre>

<h2><b>Cookies</b></h2>
<p>Cookies are small pieces of text stored in the clients browser and sent back to the server with each request. They are useful to keep some state around for more than one request (HTTP itself is stateless), but should not be used for security related stuff. They can be easily forged by the client.

All cookies sent by the client are available through BaseRequest.cookies (a FormsDict). This example shows a simple cookie-based view counter:</p>
<pre>
    <code>
    from bottle import route, request, response
    @route('/counter')
    def counter():
        count = int( request.cookies.get('counter', '0') )
        count += 1
        response.set_cookie('counter', str(count))
        return 'You visited this page %d times' % count
    </code>
</pre>
The BaseRequest.get_cookie() method is a different way do access cookies. It supports decoding signed cookies as described in a separate section.
</div>
% include templates/tailer.tpl