from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/inventory')
def inventory():
    return render_template('Inventory.html')


@app.route('/contact')
def contact():
    return render_template('contact_page.html')


if __name__ == '__main__':
    app.run()
