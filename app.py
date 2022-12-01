from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Shef<h1>'

if __name__ == '__main__':
    app.run(debug=True)

# virtualenv FLASK_APP=app.py 
# THIS ONE https://www.youtube.com/watch?v=QjtW-wnXlUY

# https://linuxhint.com/activate-virtualenv-windows/#:~:text=To%20activate%20virtualenv%20on%20Windows%2C%20first%2C%20install%20the%20pip.,%5CScripts%5Cactivate%E2%80%9D%20command.
# https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
