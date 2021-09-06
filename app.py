from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>SCA Cloud School First Task</h1><br><h2>My name is Faith Kovi.</h2><h3>Task: Writing a vagrantfile for deploying a Flask app.</h3>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
