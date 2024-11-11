import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Загрузка данных из файла при старте приложения
try:
    with open("click_data.json", "r") as file:
        data = json.load(file)
        like_count = data.get("like_count", 0)
        dontlike_count = data.get("dontlike_count", 0)
except FileNotFoundError:
    like_count = 0
    dontlike_count = 0

# Функция для сохранения данных в файл
def save_counts():
    with open("click_data.json", "w") as file:
        json.dump({"like_count": like_count, "dontlike_count": dontlike_count}, file)

# Эндпоинт для получения текущих значений
@app.route('/get_counts', methods=['GET'])
def get_counts():
    return jsonify({'like': like_count, 'dontlike': dontlike_count})

# Эндпоинт для увеличения количества "Да"
@app.route('/increment_yes', methods=['POST'])
def increment_yes():
    global like_count
    like_count += 1
    save_counts()
    return jsonify({'like': like_count})

# Эндпоинт для увеличения количества "Нет"
@app.route('/increment_no', methods=['POST'])
def increment_no():
    global dontlike_count
    dontlike_count += 1
    save_counts()
    return jsonify({'dontlike': dontlike_count})

if __name__ == '__main__':
    app.run(debug=True)