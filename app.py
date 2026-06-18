from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CD funcionando en Railway"

if __name__ == "__main__":
    app.run()