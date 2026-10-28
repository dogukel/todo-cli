import json

try:
    with open("gorevler.json", "r") as f:
        okunan = json.load(f)
except FileNotFoundError:
    okunan = []

okunan.append({"baslik": "kitap oku", "bitti": False})

with open("gorevler.json", "w") as f:
    json.dump(okunan, f, ensure_ascii=False, indent=2)

sira = 1
for gorev in okunan:
    if gorev["bitti"]:
        print(sira, ". [x] ", gorev["baslik"], sep="")
    else:
        print(sira, ". [ ] ", gorev["baslik"], sep="")
    sira+=1