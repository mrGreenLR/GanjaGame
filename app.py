from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

# Підключення до бази даних та створення таблиці, якщо вона не існує
def init_db():
    conn = sqlite3.connect('counter.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS counter (
                        id INTEGER PRIMARY KEY,
                        click_count INTEGER
                     )''')
    cursor.execute("INSERT OR IGNORE INTO counter (id, click_count) VALUES (1, 0)")
    conn.commit()
    conn.close()

# Отримати поточне значення лічильника
@app.route('/get_counter', methods=['GET'])
def get_counter():
    conn = sqlite3.connect('counter.db')
    cursor = conn.cursor()
    cursor.execute("SELECT click_count FROM counter WHERE id = 1")
    click_count = cursor.fetchone()[0]
    conn.close()
    return jsonify({'click_count': click_count})

# Оновити значення лічильника
@app.route('/update_counter', methods=['POST'])
def update_counter():
    data = request.json
    click_count = data.get('click_count', 0)
    conn = sqlite3.connect('counter.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET click_count = ? WHERE id = 1", (click_count,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

# Головна сторінка
@app.route('/')
def home():
    return render_template('index.html')  # Шаблон з файлу index.html у каталозі templates

if __name__ == '__main__':
    init_db()  # Ініціалізація бази даних
    app.run(debug=True)  # Запуск сервера в режимі налагодження
