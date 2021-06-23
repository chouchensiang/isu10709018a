from flask import Flask
main=Flask(__name__)
@main.route("/")
def index():
    return "10709018A"
@main.route("/name")
def who():
    return "jack"
if __name__ == "__main__":
    main.run()
