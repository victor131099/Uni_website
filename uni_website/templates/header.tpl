<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/styles.css">
  <title>Home</title>
</head>

<header>
  <div class="column">
    <p class="main-text">INFO2222 Project</p>
  </div>
  <div class="column">
    <a class="text" href="/home">Home</a>
    <a class="text" href="/html_content">HTML</a>
    <a class="text" href="/css">CSS</a>
    <a class="text" href="/javascript">JavaScript</a>
    <a class="text" href='/frameworks'>Web Frameworks</a>
    <a class="text" href='/bottle'>Bottle</a>
    <a class="text" href='/forum'>Forum</a>
    % if isAdmin:
        <a class="text" href='/admin'>Admin</a>
    % end
    <a class="button" href="/logout">Log Out</a>
  </div>
</header>
