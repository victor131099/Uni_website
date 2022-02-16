% include templates/header.tpl

<div class="section" id="top">
    <h1>Get Started with Web Development Today</h1>
    <p>
        Ready to learn web development? We have everything you need to get started.
    </p>
    <br>
    <a href="#topics" class="button">Get Started</a>
</div>


<div class="section">
    <h2>Introduction</h2>
    <div class="underline"></div>
    <p>Web development is a vital skill for programmers and people alike to be able to share their ideas with the world.
        It can be thought of as a medium in which website creators can interact with their audiences.
        <br>
        Having the skills of web development can allow you to share your content/information and ideas with the world;
        but more importantly, web development gives you the skills to share this in the way you want.
        In other words, you become the one designing the website, and you don't need to worry about trying to find the right WordPress theme,
        because you can simply create the one you need.
    </p>
    <br>
    <h3>What is Web Development?</h3>
    <p>Web development is the construction and design of websites.
        It is a big topic that can range from something as simple as a static web page,
        to a highly complex ecommerce platform.
    <br> Web development consists of a variety of technologies and languages.
    A website is generally split into the <strong>backend</strong> and the <strong>frontend</strong>.
    </p>

    <div class="article-container">
        <article>
            <h3>The Backend</h3>
            <img src="/img/backend.png" width="650" style="max-height:none">
            <br>
            <p>The backend of a website involves the processing of data, and serves as a means of dealing with user data and requests.
                It also serves as the gateway for a user to access the website content using the HTTP (Hyper Text Transfer) protocol.
                 The most common backend languages include PHP, Java, Python and JavaScript (thanks to Node.js);
                 however, the backend of a website can be written in almost any language.
                 <br>
                 Additionally, a database is usually used to store information that is needed by the website backend. Databases that are most commonly used include MongoDB, Postgres and SQL databases.
            </p>
            <br>
            <h3>The Frontend</h3>
            <img src="/img/frontend.jpg" width="650" style="max-height:none">
            <br>
            <p>The frontend consists of the actual design, layout and interaction that a website contains.
                This is where the user directly interacts with a website, and where the user can read content, navigate to other web pages, and more.
                <br>
                The most primary languages used for frontend design are HTML/CSS and JavaScript.
                <br>
                If you're looking to get into web development, this website will be the perfect introduction to build your skills from the ground up.
            </p>
        </article>
    </div>
    <spacer>

    <h2>Getting Started</h2>
    <div class="underline"></div>
    <div class="article-container">
        <article>
            <h3>What you'll need</h3>
            <img src="/img/computer.jpg" width="650" style="max-height:none">
            <br>
            <p>Setting up for HTML/CSS web development is quite easy, here's all that you need:
                <br>
                <br>
                A Computer
                <br>
                A Code Editing Software (Such as VSCode, Atom or Adobe DreamWeaver)
                <br>
                <br>
                You can test to make sure you're setup by copying the code below and saving it into a file called test.html.
                <br>
                <br>
                <code>
                    &lt;!DOCTYPE html&gt;
                    <br>
                    &lt;html&gt;
                    <br>
                    &lt;head&gt;
                    <br>
                    &lt;title&gt;My Website&lt;/title&gt;
                    <br>
                    &lt;/head&gt;
                    <br>
                    &lt;body&gt;
                    <br>
                    <br>
                    &lt;h1>This is a Test&lt;/h1&gt;
                    <br>
                    &lt;p>If you see this in your browser, you're ready to start learning!&lt;/p&gt;
                    <br>
                    <br>
                    &lt;/body&gt;
                    <br>
                    &lt;/html&gt;
                    <br>
                </code>
                <br>
                Once you've copied and saved the file, simply open it in your browser.
                You should see the code above transformed into a webpage! (A very simple one of course)
            </p>
        </article>
    </div>

    <div class="article-container"  id="topics">
        <article>
            <img src="/img/learnhtml.jpg">
            <h3>Getting Started with HTML</h3>
            <p>What is HTML? <br> HTML stands for Hyper Text Markup Language.
                It dictates the structure of a webpage, and provides the layout of content on a website.
            </p>
            <a href="/html" class="button">Read More</a>
        </article>
        <article>
            <img src="/img/learncss.jpg">
            <h3>Getting Started with CSS</h3>
            <p>What is CSS? <br> CSS stands for Cascading Style Sheet, and it is used to style and apply designs to the website.
                CSS can include design specifications such as font sizes, font typefaces, colours, borders, and more.
            </p>
            <a href="/css" class="button">Read More</a>
        </article>
        <article>
            <img src="/img/learnjavascript.jpg">
            <h3>Getting Started with Javascript</h3>
            <p>What is Javascript? <br> Javascript is a language that allows the extension of website functionalities.
                These functionalities include implementing dynamic elements such as videos, scroll animations or sound elements.
                Use this high-level programming language to take your website to the next level.
            </p>
            <a href="/javascript" class="button">Read More</a>
        </article>
    </div>
</div>

<div class="section" id="bottom">
    <h1>Join our discussion forum</h1>
    <p>Connect with students, create discussions, and learn about web development.</p>
    <a href="/forum" class="button">Let's Go</a>
</div>
<div class="section">
    <h2>Finished Learning Our Content?</h2>
    <p>If you need further clarification or documentation for any web technologies (including HTML and CSS),
        then <a href="https://developer.mozilla.org/en-US/">MDN Web Docs</a> is the perfect place to start.
    </p>
    <a href="https://developer.mozilla.org/en-US/" class="button">Go</a>
</div>
<div class="section" id="binary2">
    <spacer>
    <h2>Have a Question?</h2>
    <p>Try Searching our Knowledge base here</p>
    <form action="/search" method="POST">
        <input placeholder="Search" name=search type="text"></input>
        <a class="button">Go</a>
    </form>
</div>

% include templates/tailer.tpl