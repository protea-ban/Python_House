"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>查看浏览器UA</title>
  </head>
  <body>
    <div id="ua">

    </div>
    <script type="text/javascript">
      document.getElementById('ua').innerHTML = navigator.userAgent;
    </script>
  </body>
</html>
"""

from re import findall
from random import choice
from urllib.request import Request, urlopen

UAs = []

url = ''
headers = {"User-Agent": choice(UAs)}
req = Request(url, headers=headers)

with urlopen(req) as fp:
    content = fp.read().decode()

pattern = r'<div class="content">\s*?<span>\s*?(.*?)\s*?</span>'
content = findall(pattern, content)

for item in content:
    if '<a' in item:
        continue
    print(item.replace('<br/>', '\n'))
