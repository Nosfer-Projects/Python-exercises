# Using the re built-in module, extract the <html lang="en"> tag from the html text and print it to the console.


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

tag = re.findall(pattern=r'<html .*>', string=html)
print(tag[0])