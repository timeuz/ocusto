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

finalresult = (sortedresults[listkeys[0]])
print(f'Sai mais barato comprar {tipo} com o valor de R${finalresult:{4}.{3}f} por ML')