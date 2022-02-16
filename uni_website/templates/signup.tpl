<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/styles.css">
  <title>Home</title>
</head>
<div class="section" id="binary">
    <div class="module">
        <h1 class="login">Create an Account</h1>
        <form action="/signup" method="post">
            <input placeholder="University Email" name="username" type="email"><br>
            <input placeholder="First Name" name="username" type="text"><br>
            <input placeholder="Last Name" name="username" type="text"><br>
            <input placeholder="Username" name="username" type="text"><br>
            <input placeholder="Password" name="password" type="password"><br>
            <input value="Sign Up" type="submit" />
            <p style="font-size: smaller;">Already have an account? <a href="/login">Login Here</a></p>
        </form>
    </div>
</div>