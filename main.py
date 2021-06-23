from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "10709018A"
@app.route("/name")
def who():
    return "jack"
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=False)