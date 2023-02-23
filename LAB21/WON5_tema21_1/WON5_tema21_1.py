from flask import Flask, render_template
app = Flask('Water-gas Installation')

@app.route('/home')
def home():
    return render_template()