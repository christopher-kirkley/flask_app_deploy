from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1 style='color:blue'>Welcome to the Potato Farmer Website!</h1>"

if __name__ == "__main__":
    app.run('0.0.0.0')
