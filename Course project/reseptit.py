import json

reseptit = {}

reseptit["makaronilaatikko"] = []
reseptit["makaronilaatikko"].append({
    "sipuli": 1,
    "jauheliha": 400,
    "makaroni": 400,
    "lihaliemikuutio": 2,
    "maito": 10,
    "kananmuna": 2,
    "juustoraaste": 200,
    })
reseptit["makaronilaatikkoyksikot"] = []
reseptit["makaronilaatikkoyksikot"].append({
    "sipuli": "kpl",
    "jauheliha": "g",
    "makaroni": "g",
    "lihaliemikuutio": "kpl",
    "maito": "dl",
    "kananmuna": "kpl",
    "juustoraaste": "g",
    })

reseptit["pinaattiletut"] =[]
reseptit["pinaattiletut"].append({
    "pinaatti": 150,
    "kananmuna": 3,
    "vehnäjauho": 3,
    "maito": 5,
    "voi": 0.5,
    "suola": 0.5
    })
reseptit["pinaattiletutyksikot"] = []
reseptit["pinaattiletutyksikot"].append({
    "pinaatti": "g",
    "kananmuna": "kpl",
    "vehnäjauho": "g",
    "maito":"dl",
    "voi": "dl",
    "suola": "tl"
    })

reseptit["bolognese"] = [] 
reseptit["bolognese"].append({
    "sipuli": 1,
    "porkkana": 2,
    "selleri": 1,
    "valkosipulinkynsi": 1,
    "jauheliha": 400,
    "tomaattimurska": 400,
    "spagetti": 400
    })
reseptit["bologneseyksikot"] =[]
reseptit["bologneseyksikot"].append({
    "sipuli": "kpl",
    "porkkana": "kpl",
    "selleri": "kpl",
    "valkosipulinkynsi": "kpl",
    "jauheliha": "g",
    "tomaattimurska": "g",
    "spagetti": "g"
    })
  
    
with open("reseptit.txt","w") as tiedosto:
    json.dump(reseptit,tiedosto)


        
