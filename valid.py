import json

with open ("ccNasabah.json", "r") as x:
    out = json.load(x)

valid =[]
invalid = []
for i in range(len(out)):
    kontenCC = out[i].get("noCreditCard")
    if kontenCC[4] == "-":
        newKontenCC = kontenCC.replace("-","")
    else:
        newKontenCC = kontenCC
    jmlKarakter = len(list(newKontenCC))
    if jmlKarakter == 16 and int(newKontenCC[0]) in range(4,7) and newKontenCC.isdigit() is True:
        valid.append(out[i])
    else:
        invalid.append(out[i])

with open ("ccValid.json", "w") as y:
    json.dump(valid,y)

with open ("ccInvalid.json", "w") as m:
    json.dump(invalid,m)