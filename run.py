import os
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "Replace this not-to-secret key!"

@app.route('/')
def hello():
    return "Hello World!"

# export PRODUCTION=ON | OFF in TEST, and in PRODUCTION App -> Settings -> Reveal Config Vars -> KEY: PRODUCTION, VALUE: ON
if __name__ == '__main__':
    if os.environ.get("PRODUCTION") == "ON":
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=False)
    else:
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=True)
