from bs4 import BeautifulSoup

html_doc = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <nav>
        <h2>Title</h2>
        <ul>
            <li class="element1"><a href="element1">element1</a></li>
            <li class="element2"><a href="element2">element2</a></li>
            <li class="element3"><a href="element3">element3</a></li>
            <li class="element4"><a href="element4">element4</a></li>
            <li class="element5"><a href="element5">element5</a></li>
        </ul>
    </nav>
    <div>
        <p>paragraph1</p>
        <p>paragraph2</p>
        <p>paragraph3</p>
        <p>paragraph4</p>
        <p>paragraph5</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

a_elements = soup.find_all("a")

for a in a_elements:
    print(a.attrs.keys())
