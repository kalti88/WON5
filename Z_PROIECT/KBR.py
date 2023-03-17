from flask import Flask, render_template, request
import psycopg2

conn = None
try:
    conn = psycopg2.connect(host="localhost", database="KBR_database",
                            user="postgres", password="Kaltidata22")
except psycopg2.OperationalError as ex:
    print('Database error:', ex)

app = Flask('KBH')


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/furnizori/')
def suppliers():
    return render_template('furnizori.html')


@app.route('/comenzi/')
def orders():
    return render_template('comenzi.html')


@app.route('/comanda_noua/')
def new_order():
    return render_template('comanda_noua.html')


@app.route('/database/')
def database():
    return render_template('database.html')


if __name__ == '__main__':
    app.run(debug=True)