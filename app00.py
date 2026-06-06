from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Halo Flask dari GitHub"

@app.route("/api/user")
def user():
    return {
        "id": 1,
        "nama": "Tony"
    }

if __name__ == "__main__":
    app.run(debug=True)