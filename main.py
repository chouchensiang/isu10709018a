from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "10709018A"
@app.route("/name")
def who():
    return "jack"
if __name__ == "__main__":
    app.run()
