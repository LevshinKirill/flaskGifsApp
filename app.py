from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def getCurrentUrl(searchText):
    return "http://api.giphy.com/v1/gifs/search?q=" + searchText + "&api_key=BJ9cysqXzWePISsT67nRxfP2Ku0dmPQg&limit=20"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        gifs = requests.get(getCurrentUrl("cats")).json()
        return render_template("app.html", gifs=gifs['data'])
    else:
        gifs = requests.get(getCurrentUrl(request.form.get('searchText'))).json()
        return render_template("app.html", gifs=gifs['data'])


if __name__ == "__main__":
    app.run(debug=True)
