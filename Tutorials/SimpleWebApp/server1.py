from flask import Flask
from waitress import serve
import admin

if not admin.isUserAdmin():
        admin.runAsAdmin()
        
app = Flask(__name__)

if __name__ == "__main__":
    #app.run('0.0.0.0',port=server_port)
    serve(app)



# http://localhost:8000/ (Default Index)
@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, World. This is Flask"

# http://localhost:8000/abc (abc page)
@app.route("/abc", methods=["GET"])
def abc_view():
    return "Hello, World. This is abc"