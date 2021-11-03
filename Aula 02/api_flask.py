import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

lista_cidades = [
        {"cidade": "Porto Velho", "temp": 31, "escala": "celsius"},
        {"cidade": "Manaus", "temp": 29, "escala": "celsius"},
        {"cidade": "São Paulo", "temp": 14, "escala": "celsius"}
       ]

# Rota da home page
@app.route('/', methods=['GET'])
def home():
    return """<h1>Olá mundo</h1>
            <p>Esta é nossa primeira resposta de API.</p>"""

#Lista todas as cidades
@app.route('/api/v1/cidades/all', methods=['GET'])
def api_all():
    return jsonify(lista_cidades)

# Erro 404 (não encontrado)
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Nenhum resultado disponível</p>", 404

#Clima de uma cidade
@app.route('/api/v1/cidades', methods=['GET'])
def api_nome():
    if 'nome' in request.args:
        nome = request.args['nome']
    else:
        return """Erro: Não foi especificado nenhum argumento
               por favor informe o nome da cidade através do parâmetro                              'nome'."""
    cidades = []
    
    for item in lista_cidades:
        print(item)
        if item['cidade'] == nome:
            cidades.append(item)
        else:
            return page_not_found(404)

    return jsonify(cidades)

# Atualiza a lista de cidades ou uma informação de uma cidade existente.
@app.route('/api/v1/atualizar', methods=['POST','PUT'])
def api_update():
    cidade = request.form['cidade']
    temp = request.form['temp']
    escala = request.form['escala']
    if request.method == 'POST':
        lista_cidades.append({"cidade": cidade, "temp": temp, "escala": escala})
        pass
    else:
        cidades = [i['cidade'] for i in lista_cidades if 'cidade' in i]
        index = cidades.index(cidade)
        print(cidades.index(cidade))
        lista_cidades[index]["temp"] = temp
    return jsonify(lista_cidades)

# Roda o servidor
app.run()