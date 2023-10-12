from flask import Flask, request, Response, render_template, redirect, url_for
import requests
import base64
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os

app = Flask(__name__, static_folder="static")


@app.route('/bypass')
def bypass():
  link = request.args.get("link")
  link = base64.b64decode(link).decode('utf-8')
  parsed_url = urlparse(link)
  if parsed_url.scheme == 'http' or parsed_url.scheme == 'https':
    pass
  else:
    link = f'https://{link}'
  try:
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)       AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0',
        'Referer': link
    }
    raw_content = requests.get(link, headers=headers)
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
      for iframe_tag in soup.find_all('iframe', src=True):
        src = iframe_tag['src']
        encodedlink = base64.b64encode(src.encode('utf-8'))
        encodedlink = encodedlink.decode('utf-8')
        encodedlink = f'/bypass?link={encodedlink}'
        iframe_tag['src'] = encodedlink
      for imgTag in soup.find_all('img', src=True):
        src = imgTag['src']
        encodedlink = base64.b64encode(src.encode('utf-8'))
        encodedlink = encodedlink.decode('utf-8')
        bypassLink = f'/fileProxy?url={encodedlink}'
        imgTag['src'] = bypassLink
      scripts = soup.find_all('script', src=True)
      for script in scripts:
        scriptCode = requests.get(script['src'], headers=headers)
        del script['src']
        script.string = scriptCode.text
      styles = soup.find_all('link')
      for style in styles:
        href = style['href']
        encodedlink = base64.b64encode(href.encode('utf-8'))
        encodedlink = encodedlink.decode('utf-8')
        bypassLink = f'/fileProxy?url={encodedlink}'
        style['href'] = bypassLink

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
      evalscripts = '''
        scripts.forEach((script) => {
          eval(script.textContent);
        });
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
        const scripts = frame.querySelectorAll("script");
        {evalscripts}
        </script>
        </body>
        </html>
        '''
      return content
    else:
      parsed_url = urlparse(link)
      filename = os.path.basename(parsed_url.path)
      response = Response(raw_content.content, content_type=contentType)
      response.headers[
          'Content-Disposition'] = f'attachment; filename={filename}'
      return response
  except Exception as e:
    return redirect(
        url_for(
            'index',
            error=
            f"{e.__class__.__name__} occurred while trying to proxy, error details in console",
            errorDet=e))


@app.route("/")
def index():
  return render_template('index.html')


@app.route("/fileProxy")
def imageProxy():
  url = request.args.get('url', '')
  url = base64.b64decode(url).decode('utf-8')
  response = requests.get(url)
  headers = {'Content-Type': response.headers['Content-Type']}
  return Response(response.content, headers=headers)


@app.errorhandler(404)
def notFound(e):
  return redirect(url_for('index', error="error 404 page not found"))


app.run(host='0.0.0.0', port=81)
