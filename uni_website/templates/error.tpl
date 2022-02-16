% include templates/header.tpl

<!DOCTYPE html>
<html>
    <head>
    <link rel="stylesheet" href="css/styles.css" >
    <title>HTML Content</title>
    </head>

    <body>
        <div class="section" id="binary">
            <div class="module">
                <h1 class="login">404</h1>
                <h1 class="login">Page not found!</h1>
                <p>Page {{error_msg}}</p>
                <p>We couldn't find the page you were looking for. Follow the link below to return to the home page.</p>
                <a href="/home" class="button">Home Page</a>
            </div>
        </div>
    <body>

% include templates/tailer.tpl