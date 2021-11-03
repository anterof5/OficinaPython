import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Rota da home page
@app.route('/', methods=['GET'])
def home():
    return """<h1>Olá mundo</h1>
            <p>Esta é nossa primeira resposta de API.</p>"""
app.run()

#localhost:5000