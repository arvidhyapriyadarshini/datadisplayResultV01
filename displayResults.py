from flask import Flask

app = Flask(__name__)


@app.route("/")
def readLatestEntry():
    with open('https://github.com/arvidhyapriyadarshini/datadisplayResultV01/blob/main/randomTempDict3.txt', 'r') as file:
        for last_line in file:
            pass

    return last_line


if __name__ == "__main__":
    app.run()
