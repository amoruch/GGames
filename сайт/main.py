import os
from flask import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def main_page():
    with open("data.json", "rt", encoding="utf8") as f:
        data_list = json.loads(f.read())
    return render_template('base.html', data=data_list)

@app.route('/games/<name>')
def game(name):
    with open("data.json", "rt", encoding="utf8") as f:
        data_list = json.loads(f.read())
    return render_template('game_page.html', data=data_list[name])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
