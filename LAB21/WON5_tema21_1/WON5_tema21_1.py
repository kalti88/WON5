from flask import Flask

app = Flask('Water-gas Installation')


@app.route('/')
@app.route('/home')
def home():
    return 'Wellcome! Website under construction'


@app.route('/portfolio')
def portfolio():
    return 'Coming soon!'


if __name__ == '__main__':
    app.run(debug=True)
