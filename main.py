from flask import Flask, request, Response
import requests
import base64
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os

app = Flask(__name__)


def is_html(string):
  html_tags = ["<html", "<head", "<body", "<div", "<p", "<a", "<span"]
  for tag in html_tags:
    if tag in string:
      return True
  return False


@app.route('/bypass')
def bypass():
  link = request.args.get("link")
  link = base64.b64decode(link).decode('utf-8')
  raw_content = requests.get(link)
  contentType = raw_content.headers.get('content-type', '').lower()
  if 'text/html' in contentType:
    soup = BeautifulSoup(raw_content.text, 'html.parser')
    for tag in soup.find_all(href=True):
      href = tag['href']
      parsed_href = urlparse(href)
      if not parsed_href.scheme or not parsed_href.netloc:
        public_link = urljoin(link, href)
        tag['href'] = public_link
      else:
        pass
    for tag in soup.find_all(src=True):
      src = tag['src']
      parsed_src = urlparse(src)
      if not parsed_src.scheme or not parsed_src.netloc:
        public_link = urljoin(link, src)
        tag['src'] = public_link
    for a_tag in soup.find_all('a', href=True):
      href = a_tag['href']
      encodedlink = base64.b64encode(href.encode('utf-8'))
      encodedlink = encodedlink.decode('utf-8')
      encodedlink = f'/bypass?link={encodedlink}'
      a_tag['href'] = encodedlink
    content = base64.b64encode(soup.prettify().encode('utf-8'))
    webchanger = '''
        <input id="link"></input>
      <button id="submit">change website</button>
      <script>
      const button = document.getElementById("submit");
      const link = document.getElementById("link");
      button.addEventListener("click", function() {
          data = btoa(link.value)
          window.location.href = "/bypass?link=" + data;
      });
      </script>
    '''
    content = f'''
      <html>
      <head>
      <meta charset="UTF-8">
      </head>
      <body>
      {webchanger}
      <div id="frame">
      </div>
      <script>
      const frame = document.getElementById("frame");
      let content = "{content.decode('utf-8')}";
      content = atob(content);
      frame.innerHTML = content;
      </script>
      </body>
      </html>
      '''
    return content
  else:
    parsed_url = urlparse(link)
    filename = os.path.basename(parsed_url.path)
    response = Response(raw_content.content, content_type=contentType)
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    return response


@app.route("/")
def index():
  return '''
  <html>
    <head>
    <meta charset="UTF-8">
    </head>
    <body>
    <input id="link"></input>
    <button id="submit">bypass</button>
    <script>
    const button = document.getElementById("submit");
    const link = document.getElementById("link");
    button.addEventListener("click", function() {
        data = btoa(link.value)
        window.location.href = "/bypass?link=" + data;
    });
    </script>
    </body>
    </html>
  '''


app.run(host='0.0.0.0', port=81)
