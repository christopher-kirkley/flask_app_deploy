from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1 style='color:blue'>Now do something different to this to his thisajdslfkahjsfljkasl;dfjadsf to the Potato Farmer Website!</h1>"

if __name__ == "__main__":
    app.run('0.0.0.0')
