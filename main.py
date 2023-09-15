from flask import Flask, request
import requests
import base64

app = Flask(__name__)


@app.route('/bypass')
def bypass():
  link = request.args.get("link")
  content = requests.get(base64.b64decode(link))
  content = base64.b64encode(content.content)
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
