% include templates/header.tpl

<div style="margin-top:120px">
<h1 class = "textTitle" style = "padding-left: 500px;">User Input</h1>
<div>
    <p>
        JavaScript has several methods that you can use to interact with users. For example, we want the user to enter a name or other personal information. In this case, we can use the Windows.prompt () method.
    </p>
    <pre>
        <code>
            &lt;!DOCTYPE html&gt;
            &lt;html&gt;
            &lt;body&gt;
            &lt;p>Click the button to demonstrate the prompt box.&lt;/p&gt;
            &lt;button onclick="myFunction()">Try it&lt;/button&gt;
            &lt;p id="demo">&lt;/p&gt;

        </code>
    </pre>
    <div>
        <p>
            Next, let's add the script tag to allow us to run JavaScript on the page.
        </p>
        <pre>
            <code>
            &lt;script&gt;
                function myFunction() {
                var person = prompt("Please enter your name");
                if (person != null) {
                    document.getElementById("demo").innerHTML =
                    "Hello " + person + "! How are you today?";
                  }
                }

            &lt;/script&gt;
            </code>
        </pre>
    </div>
</div>

% include templates/tailer.tpl