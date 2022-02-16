% include templates/header.tpl

<div style="margin-top:120px">
<h1 class = "textTitle" style = "padding-left: 500px;">Creating buttons with Events</h1>
<div>
    <p>
        A simple way to create a button is to use the HTML tag

    </p>
    <pre>
        <code>
            &lt;button&gt; This is a button  &lt;/button&gt;


        </code>
    </pre>
    <div>
        <p>
            However, to make it reactive to user input you must add JavaScript. To make the button reactive to use clicks, change the button and add the following JavaScript
        </p>
        <pre>
            <code>
                &lt;button onclick="helloWorld()"&gt;Click me!&lt;/button&gt;
                &lt;script&gt;
                function helloWorld() {
                    alert("Hello World!");
                }
                &lt;/script&gt;
            </code>
        </pre>
    </div>
    <div>
        <p>This results in the final HTML and JavaScript:</p>
        <pre>
            <code>
            &lt;html&gt;
                &lt;body&gt;
                    &lt;h1&gt;
                        Button demo
                    &lt;/h1&gt;
                    &lt;button onclick="helloWorld()"&gt;Click me!&lt;/button&gt;
                    &lt;script&gt;
                        function helloWorld() {
                            alert("Hello World!");
                        }
                    &lt;/script&gt;
                &lt;/body&gt;
            &lt;/html&gt;
            </code>
        </pre>
    </div>
</div>

% include templates/tailer.tpl