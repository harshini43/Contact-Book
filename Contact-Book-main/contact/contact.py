<!DOCTYPE html>
<html>
<head>
  <title>Login Page</title>
  <style>
    /* Add some style to the page */
    body {
      font-family: Arial, sans-serif;
	backgroundimage:url('back.png');color:black;text-	align:center; 
    }

    /* Center the form and give it some margin */
    .form-container {
      width: 400px;
      margin: 50px auto;
      padding: 20px;
      border: 1px solid #ccc;
      background-color: #fff;
    }

    /* Style the input fields and the button */
    input[type=text], input[type=password], button {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      display: inline-block;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }

    button {
      background-color: #04AA6D;
      color: white;
      border: none;
      cursor: pointer;
    }

    button:hover {
      opacity: 0.8;
    }

    /* Style the labels */
    label {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Welcome</h2>
    <form action="/action_page.php" method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" placeholder="Enter your username" required>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" placeholder="Enter your password" required>
      <button type="submit">Login</button>
    </form>
  </div>
</body>
</html>