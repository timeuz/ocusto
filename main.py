from flask import Flask, render_template, request

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

    result = {
        "litrao": 0,
        "seisct": 0,
        "quinci": 0,
        "trezcc": 0,
        "trezci": 0,
        "treznt": 0
    }

    result["litrao"] = float(input("LITRAO: "))
    result["seisct"] = float(input("600: "))
    result["quinci"] = float(input("550: "))
    result["trezcc"] = float(input("355: "))
    result["trezci"] = float(input("350: "))
    result["treznt"] = float(input("300: "))

    for x in result.keys():
        print(x)
        match x:
            case "litrao":
                result[x] = result[x]/1000
                print("to no litrao")
            case "seisct":
                result[x] = result[x]/600
                print("to no seisct")
            case "quinci":
                result[x] = result[x]/550
                print("to no quinci")
            case "trezcc":
                result[x] = result[x]/355
                print("to no trezcc")
            case "trezci":
                result[x] = result[x]/350
                print("to no trezci")
            case "treznt":
                result[x] = result[x]/300
                print("to no treznt")

    sortedresults = sorted(result.items(), key=lambda x:x[1])
    sortedresults = dict(sortedresults)

    for z in list(sortedresults):
        if sortedresults[z] == 0.0:
            del sortedresults[z]

    print(sortedresults)

        # result = float(f'{result:.2f}')
    
    return render_template("cerv.html",
                          resultado = sortedresults[0],
                          gasolina = gasolina,
                          result = result,
                          comp = comp
                          )

@app.route('/refri', methods=['GET', 'POST'])
def calcrefri():
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
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)