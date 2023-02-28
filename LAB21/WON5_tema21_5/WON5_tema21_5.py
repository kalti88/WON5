from flask import Flask, render_template

app = Flask('Water-gas Installation')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portofoliu')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


if __name__ == '__main__':
    app.run(debug=True)
