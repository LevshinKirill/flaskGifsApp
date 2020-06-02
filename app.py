import flask
import requests

app = flask.Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        gifs = requests.get("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=BJ9cysqXzWePISsT67nRxfP2Ku0dmPQg&limit=20").json()
        return flask.render_template("app.html", gifs=gifs['data'])
    else:
        gifs = requests.get("http://api.giphy.com/v1/gifs/search?q="+flask.request.form.get('searchText')+"&api_key=BJ9cysqXzWePISsT67nRxfP2Ku0dmPQg&limit=20").json()
        return flask.render_template("app.html", gifs=gifs['data'])

if __name__ == "__main__":
    app.run(debug=True)