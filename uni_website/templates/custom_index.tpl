% include templates/header.tpl

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/styles.css">
    <title>Home</title>
</head>

<body>
    <header>
        <div class="column">
            <p class="main-text">INFO2222 Project</p>
        </div>
        <div class="column">
            <a class="text">HTML</a>
            <a class="text">CSS</a>
            <a class="text">Web Frameworks</a>
            <a class="text">Support</a>
            <a class="button" href="">Sign In</a>
        </div>
    </header>
    <div class="section" id="top">
        <h1>Get Started with Web Development Today</h1>
        <p>Ready to learn web development? We have everything you need to get started.</p>
        <br>
        <a class="button">Get Started</a>
    </div>
    <div class="section">
        <h2>Featured</h2>
        <div class="underline"></div>
        <div class="article-container">
            <article>
                <img src="../images/code.png">
                <h3>Getting Started with HTML</h3>
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                    industry's standard
                    dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
                    make a type specimen
                    book. It has survived not only five centuries, but also the leap into electronic typesetting,
                    remaining essentially
                    unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
                    Ipsum passages, and more
                    recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                </p>
                <a class="button">Read More</a>
            </article>
            <article>
                <img src="../images/code.png">
                <h3>Getting Started with HTML</h3>
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                    industry's standard
                    dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
                    make a type specimen
                    book. It has survived not only five centuries, but also the leap into electronic typesetting,
                    remaining essentially
                    unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
                    Ipsum passages, and more
                    recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                </p>
                <a class="button">Read More</a>
            </article>
            <article>
                <img src="../images/code.png">
                <h3>Getting Started with HTML</h3>
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                    industry's standard
                    dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
                    make a type specimen
                    book. It has survived not only five centuries, but also the leap into electronic typesetting,
                    remaining essentially
                    unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
                    Ipsum passages, and more
                    recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                </p>
                <a class="button">Read More</a>
            </article>
        </div>
    </div>
    <div class="section" id="bottom">
        <h1>Search Our Knowledge Base</h1>
        <p>Connect with students, create discussions, and learn about web development.</p>
        <a class="button">Let's Go</a>
    </div>
    <div class="section">
        <h2>Have a Question?</h2>
        <p>Try Searching our Knowledge base here</p>
        <form>
            <input placeholder="Search" name=search type="text"></input>
            <a class="button">Go</a>
        </form>
    </div>

    <footer>
        <div class="column">
            <h2>INFO2222 PROJECT</h2>
            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                industry's standard
                dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
                make a type specimen
                book.</p>
        </div>
        <div class="column">
            <h2>Resources</h2>
            <a>HTML</a>
            <a>CSS</a>
            <a>Web Frameworks</a>
            <a>Support</a>
        </div>
        <div class="column">
            <h2>Knowledge Base</h2>
            <a>Link 1</a>
            <a>Link 2 </a>
            <a>Link 3</a>
            <a>Link 4</a>
        </div>
    </footer>
</body>

</html>

% include templates/tailer.tpl