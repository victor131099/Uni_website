% include templates/header.tpl

<div style="margin-top:120px">
<h1 class = "textTitle" style = "padding-left: 500px;">Updating Text</h1>
<div>
    <p>
        Updating text using JavaScript can be an important task, especially when combined with form validation, or any other component of a website that requires dynamically changing content.
        To begin, we're going to create a simple html page, with some text:
    </p>
    <pre>
        <code>
            &lt;!DOCTYPE html&gt;
            &lt;html lang="en"&gt;
            &lt;head&gt;
            &lt;meta charset="UTF-8"&gt;
            &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
            &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
            &lt;title"&gt;Updating Text with JavaScript&lt;/title&gt
            &lt;/head&gt;
            &lt;body&gt;
            &lt;p&gt;Here is some text that needs to change!&lt;/p&gt;
            &lt;/body&gt;
            &lt;/html&gt;
        </code>
    </pre>
    <div>
        <p>
            Next, let's add the script tag to allow us to run JavaScript on the page.
        </p>
        <pre>
            <code>
            &lt;script type="text/javascript"&gt;
                console.log("JavaScript is Running on this page!");
            &lt;/script&gt;
            </code>
        </pre>
    </div>
</div>

% include templates/tailer.tpl