from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_url_path='/projects/ocusto/static')

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
                          comp = comp
                          )

@app.route('/cerva', methods=['GET', 'POST'])
def calccerva():
    resultado = ""
    result = {
        "litrao": 0,
        "seisct": 0,
        "quinci": 0,
        "trezcc": 0,
        "trezci": 0,
        "treznt": 0
    }
    if request.method == 'POST':
        result = {
            "litrao": float(request.form['litrao']),
            "seisct": float(request.form['seisct']),
            "quinci": float(request.form['quinci']),
            "trezcc": float(request.form['trezcc']),
            "trezci": float(request.form['trezci']),
            "treznt": float(request.form['treznt'])
        }

        for x in result.keys():
            match x:
                case "litrao":
                    result[x] = result[x]/1000
                case "seisct":
                    result[x] = result[x]/600
                case "quinci":
                    result[x] = result[x]/550
                case "trezcc":
                    result[x] = result[x]/355
                case "trezci":
                    result[x] = result[x]/350
                case "treznt":
                    result[x] = result[x]/300

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
            case "quinci":
                tipo = "Garrafa de 550ml"
            case "trezcc":
                tipo = "Lata de 355ml"
            case "trezci":
                tipo = "Lata de 350ml"
            case "treznt":
                tipo = "Lata de 300ml"

        resultado = (sortedresults[listkeys[0]])
        resultado = (f'Sai mais barato comprar {tipo} com o valor de R${resultado:{4}.{3}f} por ML')

    return render_template(
            "cerv.html",
            resultado = resultado,
            litrao = result["litrao"],
            seisct = result["seisct"],
            quinci = result["quinci"],
            trezcc = result["trezcc"],
            trezci = result["trezci"],
            treznt = result["treznt"]
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

@app.route('/api/refri')
def apicomb():
    etanol = float(request.args.get('etanol'))
    gasolina = float(request.args.get('gasolina'))
    result = 0
    comp = 0.73
    if etanol != 0.0 and gasolina != 0.0:
        result = (etanol / gasolina)
        result = float(f'{result:.2f}')

    return render_template("comb.html",
                          etanol = etanol,
                          gasolina = gasolina,
                          result = result,
                          comp = comp
                          )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)