#!/usr/bin/pyhton3
"""Hello Flask! (Task 0)

make server visible across all networks
listen on 0.0.0.0:5000
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Task 0 """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
