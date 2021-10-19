from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "setup later"

@app.route("/")
def home():
    return "<h1>Čia mano naujas puslapis</h1>"

if __name__ == "__main__":
    app.run(debug=True)