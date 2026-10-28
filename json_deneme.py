import json

gorevler = [
    {"baslik" : "süt al", "bitti" : False},
    {"baslik" : "README yaz", "bitti" : True},
    {"baslik" : "spor yap", "bitti": False},
]

with open("gorevler.json", "w") as f:
    json.dump(gorevler, f, ensure_ascii=False, indent=2)

with open("gorevler.json", "r") as f:
    okunan = json.load(f)

sira = 1
for gorev in okunan:
    if gorev["bitti"]:
        print(sira, ". [x] ", gorev["baslik"], sep="")
    else:
        print(sira, ". [ ]", gorev["baslik"], sep="")
    sira+=1