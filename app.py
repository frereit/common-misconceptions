import random
from typing import List

import wikipedia
from flask import Flask, render_template, jsonify

app = Flask(__name__)


def get_all_misconceptions() -> List[str]:
    article = wikipedia.page("list_of_common_misconceptions")
    content = article.content.split("== See also ==")[0]  # Exclude references etc
    parsed = []
    for line in content.split("\n"):
        if (
            not line.startswith("=") and len(line.strip()) != 0
        ):  # not a title and not empty
            parsed.append(line)
    return parsed[2:]  # remove the descriptor lines


MISCONCEPTIONS = get_all_misconceptions()


@app.route("/")
def random_misconception():
    return render_template(
        "misconception.html", misconception=random.choice(MISCONCEPTIONS)
    )


@app.route("/random")
def random_misconception_raw():
    return random.choice(MISCONCEPTIONS)


@app.route("/all.json")
def all_misconceptions_raw():
    return jsonify(MISCONCEPTIONS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
