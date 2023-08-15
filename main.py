import json
from flask import Flask, request, jsonify
from SRI import obtenerdatos

app = Flask(__name__)


@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    # Obtiene los datos de los parámetros de la solicitud POST
    ruc = request.args.get('ruc')
    contraseña = request.args.get('contraseña')
    año = request.args.get('año')
    mes = request.args.get('mes')
    dia = request.args.get('dia')
    obtenerdatos(ruc, contraseña, año, mes, dia)
    with open('tabla_data.json', 'r') as file:
        datos = json.load(file)
    return jsonify(datos)

if __name__ == "__main__":
    app.run(debug=True)