from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')
URLBASE="https://timeu.com.br/ocusto"
@app.route('/')
def index():
    return render_template('index.html', URLBASE=URLBASE)

@app.route('/combustivel', methods=['GET', 'POST'])
def calccomb():
    etanol = 0
    gasolina = 0
    result = 0
    comp = 0.73
    if request.method == 'POST':
        etanol = float(request.form['etanol'])
        gasolina = float(request.form['gasolina'])
        result = (etanol / gasolina)
        result = float(f'{result:.2f}')

    return render_template("comb.html",
                          etanol = etanol,
                          gasolina = gasolina,
                          result = result,
                          comp = comp,
                          URLBASE=URLBASE
                          )

@app.route('/cerva', methods=['GET', 'POST'])
def calccerva():
    resultado = ""
    result = {
        "litrao": 0,
        "seisct": 0,
        "latao": 0,
        "trezcc": 0,
        "trezci": 0,
        "duzsen": 0
    }
    if request.method == 'POST':
        result = {
            "litrao": float(request.form['litrao']),
            "seisct": float(request.form['seisct']),
            "latao": float(request.form['latao']),
            "trezcc": float(request.form['trezcc']),
            "trezci": float(request.form['trezci']),
            "duzsen": float(request.form['duzsen'])
        }

        for x in result.keys():
            match x:
                case "litrao":
                    result[x] = result[x]/1000
                case "seisct":
                    result[x] = result[x]/600
                case "latao":
                    result[x] = result[x]/473
                case "trezcc":
                    result[x] = result[x]/355
                case "trezci":
                    result[x] = result[x]/350
                case "duzsen":
                    result[x] = result[x]/269

        sortedresults = sorted(result.items(), key=lambda x:x[1])
        sortedresults = dict(sortedresults)

        for z in list(sortedresults):
            if sortedresults[z] == 0.0:
                del sortedresults[z]

        listkeys = list(sortedresults.keys())

        match listkeys[0]:
            case "litrao":
                tipo = "Litrão"
            case "seisct":
                tipo = "Garrafa de 600ml"
            case "latao":
                tipo = "Latão de 473ml"
            case "trezcc":
                tipo = "Lata de 355ml"
            case "trezci":
                tipo = "Lata de 350ml"
            case "duzsen":
                tipo = "Lata de 269ml"

        resultado = (sortedresults[listkeys[0]])
        resultado = (f'Sai mais barato comprar {tipo} com o valor de R${resultado:{4}.{3}f} por ML')

    return render_template(
            "cerv.html",
            resultado = resultado,
            litrao = result["litrao"],
            seisct = result["seisct"],
            latao = result["latao"],
            trezcc = result["trezcc"],
            trezci = result["trezci"],
            duzsen = result["duzsen"],
            URLBASE=URLBASE
        )

# @app.route('/refri', methods=['GET', 'POST'])
# def calcrefri():
#     etanol = 0
#     gasolina = 0
#     result = 0
#     comp = 0.73
#     if request.method == 'POST':
#         etanol = float(request.form['etanol'])
#         gasolina = float(request.form['gasolina'])
#         result = (etanol / gasolina)
#         result = float(f'{result:.2f}')

#     return render_template("comb.html",
#                           etanol = etanol,
#                           gasolina = gasolina,
#                           result = result,
#                           comp = comp
#                           )

############################ API Methods #################################

@app.route('/api/combustivel')
def apicomb():
    etanol = float(request.args.get('etanol'))
    gasolina = float(request.args.get('gasolina'))
    result = 0
    comp = 0.73

    if etanol != 0.0 and gasolina != 0.0:
        result = (etanol / gasolina)
        result = float(f'{result:.2f}')

    if result <= comp:
        combustivel = "Etanol"
    else:
        combustivel = "Gasolina"

    final_result = {
        "etanol": etanol,
        "gasolina": gasolina,
        "razao": result,
        "resultado": combustivel
    }
    return jsonify(final_result)

if __name__ == '__main__':
    app.run()
