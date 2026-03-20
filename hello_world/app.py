from flask import Flask

app = Flask(__name__)

@app.route("/") #home or root of site
def index():
    #return "UwU Hello World"
    return '<html><head><title>Hello UwU World</title></head><body><h1>Hello World</h1><img src="Cirno.GIF" width="300" height="200"><p> Ir a <a href="/about">About</a></p></body></html>'

@app.route("/about")
def about():
    #return 'About page'
    return '<html><head><title>About this page</title></head><body><h1>Everything about this website. Back to <a href="/">Hello UwU world</a><body></html>'

if __name__ == "__main__":
    app.run(debug=True)