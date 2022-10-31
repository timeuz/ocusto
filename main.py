from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
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
    
    return render_template("index.html",
                          etanol = etanol,
                          gasolina = gasolina,
                          result = result,
                          comp = comp
                          )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)