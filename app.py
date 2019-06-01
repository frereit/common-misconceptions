import random

import wikipedia
from flask import Flask, render_template, jsonify

app = Flask(__name__)


misconceptions = []


def get_all_misconceptions() -> [str]:
    article = wikipedia.page("list_of_common_misconceptions")
    content = article.content.split("== See also ==")[0]  # Exclude references etc
    parsed = []
    for line in content.split("\n"):
        if not line.startswith("=") and len(line.strip()) != 0:  # not a title and not empty
            parsed.append(line)
    return parsed[1:]  # remove the descriptor line


@app.before_first_request
def load_misconceptions():
    global misconceptions
    misconceptions = get_all_misconceptions()


@app.route('/')
def random_misconception():
    return render_template("misconception.html", misconception=random.choice(misconceptions))


@app.route('/random')
def random_misconception_raw():
    return random.choice(misconceptions)


@app.route('/all.json')
def all_misconceptions_raw():
    return jsonify(misconceptions)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
