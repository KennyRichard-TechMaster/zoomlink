from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "El Royal Link Service Running"

@app.route("/zoom")
def zoom():
    return redirect("https://us06web.zoom.us/meeting/register/b8XGsaaCTiW18Ca7Az_qtg")

if __name__ == "__main__":
    app.run()