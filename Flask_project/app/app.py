import sqlite3
import os
from flask import Flask, render_template, request


DATABASE = '/tmp/batabase.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'database.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def close_db(conn):
    conn.close()


@app.route('/')
def menu():
    conn = connect_db()
    conn.close()
    return render_template('menu.html')

def init_db():
    conn = connect_db()
    conn.execute('CREATE TABLE IF NOT EXISTS trip (distance FLOAT NOT NULL, fuel_consumption FLOAT NOT NULL, '
                 'fuel_price FLOAT NOT NULL)')
    conn.close()

@app.before_request
def before_first_request():
    init_db()

@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        distance = request.form["distance"]
        fuel_consumption = request.form["fuel_consumption"]
        fuel_price = request.form["fuel_price"]
        conn = connect_db()
        conn.execute('INSERT INTO trip (distance, fuel_consumption, fuel_price) VALUES (?, ?, ?)',
                     (distance, fuel_consumption, fuel_price))
        conn.commit()
        conn.close()
        result = (float(distance)/100) * float(fuel_consumption) * float(fuel_price)
        print_ = f'Стоимость поездки составит {int(result)} рублей! Удачи на дорогах!'
        return render_template('index.html', print_=print_)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)