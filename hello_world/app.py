from flask import Flask

app = Flask(__name__)

@app.route("/") #home or root of site
def index():
    return "UwU Hello World"

@app.route("/about")
def about():
    return 'About page'

if __name__ == "___main__":
    app.run(debug=True)