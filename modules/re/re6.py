# Using the re built-in module, extract all tags from the html text in the form of a list. Print each tag on a separate line to the console.

import re


html = """<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Title</title>
  <meta name="description">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
</body>
</html>"""

for tag in re.findall(r"<.*>", html):
    print(tag)