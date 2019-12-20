from flask import Flask, render_template, request, redirect, url_for, flash
import pygal
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from Config.Config import Production

app = Flask(__name__)
app.config.from_object(Production)

db = SQLAlchemy(app)

from models.inventories import Inventories
from models.sales import Sales


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/salepro/<int:inv_id>', methods=['POST', 'GET'])
def make_sales(inv_id):
    record = Inventories.fetch_one_record(inv_id)
    if record:
        if request.method == 'POST':
            quantity = request.form['quantity']
            new_stock = record.stock - int(quantity)
            record.stock = new_stock
            db.session.commit()
            sales = Sales(inv_id=inv_id, quantity=quantity)
            sales.add_records()

        flash('You successfully made a sale', 'success')
    return redirect(url_for('inventory'))


@app.route('/view_sales/<int:inv_id>')
def view_sales(inv_id):
    record = Inventories.fetch_one_record(inv_id)
    return render_template('sales.html', record=record)


@app.route('/inventory', methods=['POST', 'GET'])
def inventory():
    records = Inventories.fetch_all_records()
    return render_template('inventory.html', records=records)


@app.route('/add_inventory', methods=['POST', 'GET'])
def add_inv():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        stock = request.form['stock']
    record = Inventories(name=name, category=category, buying_price=buying_price,
                         selling_price=selling_price, stock=stock)
    record.add_records()
    return redirect(url_for('inventory'))


@app.route('/sale/<int:inv_id>', methods=['POST', 'GET'])
def makeSale(inv_id):
    rec = Inventories.fetch_one_record(inv_id)
    if rec:
        if request.method == 'POST':
            newStock = rec.stock - int(request.form['quantity'])
            rec.stock = newStock
            db.session.commit()
        # saleRecord = Sales(inv_id=inv_id, quantity=)
    return redirect(url_for('inventory'))


@app.route('/delete/<int:inv_id>', methods=['POST', 'GET'])
def delete(inv_id):
    record = Inventories.fetch_one_record(inv_id)
    db.session.delete(record)
    db.session.commit()
    # flash("Item Deleted", 'danger')
    return redirect(url_for('inventory'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/edit/<int:inv_id>', methods=['POST', 'GET'])
def edit(inv_id):
    record = Inventories.fetch_one_record(inv_id)

    if request.method == 'POST':
        record.name = request.form['name']
        record.category = request.form['category']
        record.buying_price = request.form['buying_price']
        record.selling_price = request.form['selling_price']
        record.stock = request.form['stock']
        db.session.commit()
        return redirect(url_for('inventory'))
    return render_template('edit.html', record=record)


@app.route('/contact')
def contact():
    return render_template('contact_page.html')


@app.route('/dashboard')
def piechart():
    ratios = [("men", 5), ("ladies", 9)]
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add(ratios[0][0], ratios[0][1])
    pie_chart.add(ratios[1][0], ratios[1][1])
    # pie_chart.add('Chrome', 36.3)
    # pie_chart.add('Safari', 4.5)
    # pie_chart.add('Opera', 2.3)
    pie_data = pie_chart.render_data_uri()
    dt = [
        {'month': 'Jan', 'total': 22}, {'month': 'Feb', 'total': 27}, {'month': 'Mar', 'total': 23},
        {'month': 'Apr', 'total': 20}, {'month': 'May', 'total': 12},
    ]
    s = [d['month'] for d in dt]
    x = [v['total'] for v in dt]

    graph = pygal.Line()
    graph.title = '% Change Coolness of programming languages over time.'
    graph.x_labels = s
    graph.add('total', x)
    # graph.add('Java', [15, 45, 76, 80, 91, 95])
    # graph.add('C++', [5, 51, 54, 102, 150, 201])
    # graph.add('All others combined!', [5, 15, 21, 55, 92, 105])
    graph_data = graph.render_data_uri()
    return render_template('dashboard.html', pie_data=pie_data, graph_data=graph_data)


if __name__ == '__main__':
    app.run()
