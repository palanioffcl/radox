from src.main import *
from utils.srv_info import *
from wsgiref.simple_server import make_server

app = radox()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/palani")
def index(request):
    return "Hello World"

if __name__=='__main__':
    server = make_server('127.0.0.1', 3301, app)
    info()
    server.serve_forever()
