import sqlite3
import os
from flask import Flask, render_template, request


DATABASE = '/tmp/batabase.db'
"""Путь к файлу базы данных (по умолчанию)."""
DEBUG = True

app = Flask(__name__)
"""Объект Flask приложения."""
app.config.from_object(__name__)
"""Загрузка конфигурации из текущего модуля."""

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'database.db')))
"""Обновление конфигурации с путем к базе данных."""

def connect_db():
    """
     Подключается к базе данных SQLite.

    Returns:
        sqlite3.Connection: Подключение к базе данных.
    """
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def close_db(conn):
    """
    Закрывает соединение с базой данных.

    Args:
        conn (sqlite3.Connection): Подключение к базе данных.
    """
    conn.close()


@app.route('/')
def menu():
    """
    Обработчик маршрута '/' (главное меню).

    Returns:
        flask.templating.render_template: Рендерит шаблон 'menu.html'.
    """
    conn = connect_db()
    conn.close() # Закрытие соединения после использования!
    return render_template('menu.html')


# def init_db():
#     """Инициализирует базу данных, создавая таблицу 'trip'."""
#     conn = connect_db()
#     cursor = conn.cursor()  # Get a cursor object
#
#     cursor.execute('''
#         SELECT name FROM pragma_table_info('trip')
#         WHERE name IN ('point_a', 'point_b');
#     ''')
#     existing_columns = cursor.fetchall()
#
#     if not existing_columns: #Check if columns are present.
#         cursor.execute('''
#             ALTER TABLE trip
#             ADD COLUMN point_a STRING;
#         ''')
#         cursor.execute('''
#             ALTER TABLE trip
#             ADD COLUMN point_b STRING;
#         ''')
#         conn.commit()  #Commit changes
#
#     conn.close()


def init_db():
    """
    Инициализирует базу данных, создавая таблицу 'trip', если она не существует.
    """
    conn = connect_db()
    conn.execute('CREATE TABLE IF NOT EXISTS trip (distance FLOAT NOT NULL, fuel_consumption FLOAT NOT NULL, '
                 'fuel_price FLOAT NOT NULL, point_a STRING, point_b STRING)')
    conn.commit()  # Добавлен commit для сохранения изменений в БД
    conn.close()


@app.before_request
def before_first_request():
    """
    Выполняет инициализацию базы данных перед первым запросом к приложению.
    """
    init_db()


@app.route('/index/', methods=['GET', 'POST'])
def index():
    """
    Обработчик маршрута '/index/', обрабатывает GET и POST запросы.

    GET запрос отображает форму. POST запрос обрабатывает данные формы, сохраняет их в БД и отображает результат.

    Returns:
        flask.templating.render_template: Рендерит шаблон 'index.html' с данными или без.
    """
    if request.method == 'POST':
        distance = request.form["distance"]
        fuel_consumption = request.form["fuel_consumption"]
        fuel_price = request.form["fuel_price"]
        point_a = request.form["point_a"]
        point_b = request.form["point_b"]
        conn = connect_db()
        conn.execute('INSERT INTO trip (point_a, point_b, distance, fuel_consumption, fuel_price) '
                     'VALUES (?, ?, ?, ?, ?)', (point_a, point_b, distance, fuel_consumption, fuel_price))
        conn.commit()
        conn.close()
        result = (float(distance)/100) * float(fuel_consumption) * float(fuel_price)
        print_1 = (f'Вы поедете из {point_a} в {point_b}.')
        print_2 = (f'Стоимость поездки составит {int(result)} рублей!')
        print_3 = (f'Удачи на дорогах!')
        return render_template('index.html', print_1=print_1, print_2=print_2, print_3=print_3)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
