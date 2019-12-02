from flask import Flask, render_template
import pygal

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
