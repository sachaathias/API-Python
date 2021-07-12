import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Website</h3><p>This site is a prototype API</p>"

@app.route('/eric', methods=['GET'])
def second():
    return "<h1>Hello</h3><p>This site is a prototype API</p>"

app.run()
