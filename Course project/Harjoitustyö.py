import json
def reseptikone():
    lista =[]
    listakaksi =[]
    aineosat = []
    logo =""" 
    ___     ___   ___   ___   ___   _____        
    |  \   |     |     |     |   |    |    |    
    |__/   |___  |___  |___  |___|    |    |
    |  \   |         | |     |        |    |  
    |   \  |___   ___| |___  |        |    |
            ____            ___     
    |  /   |    |  |\   |  |              
    |_/    |    |  | \  |  |___
    | \    |    |  |  \ |  |
    |  \   |____|  |   \|  |___       v.1.0
    """    
    print(logo)
    print("""
Tervetuloa käyttämään reseptikonetta!

Reseptikoneen avulla voit muuntaa tutut reseptit suhteessa valitsemaasi aineosaan.
Voit myös lisätä oman reseptin kirjoittamalla "oma" ensimmäiseen kysymyskenttään
(Huom. tämä ylikirjoittaa olemassa olevan oman reseptin.)""")
    print("")
    
    with open("reseptit.txt","r") as tiedosto:
        data= json.load(tiedosto)
    with open("omaresepti.txt","r") as omaresepti:
        omadata= json.load(omaresepti)
 
    reseptit = []
    omatreseptit =[]
    for resepti in (data.keys()):
        reseptit.append(resepti)
    print("Perinteiset: ")
    
    for i in range(0,len(reseptit),2):
        print("-",reseptit[i])
        
    for omaresepti in (omadata.keys()):
        omatreseptit.append(omaresepti)
    print("")
    print("Oma resepti: ")
    
    for i in range(0,len(omatreseptit),2):
        print("-",omatreseptit[i]) 
    print("")

    def valinta(resepti,data):
            for i in data[resepti]:
                for j in i.values():
                    lista.append(j)
                return(lista)
            
    def yksikot(a,data):
        for i in data[a]:
            for j in i.values():
                listakaksi.append(j)
            return(listakaksi)
        
    def index(a,aineosat,data):
        for i in data[a]:
            for j in i:
                aineosat.append(j)
            return(aineosat)
            
    def omaresepti(a) :
        taulu ={a[i]: a[i+1] for i in range(0, len(a), 2)}
        return(taulu)
        
    while True:
        resepti = input("Mikä resepti? :")
        if resepti in data:
            break
        if resepti in omadata:
            break
        if resepti == "oma":
            break
        print("Reseptiä ei löytynyt. Valitse listasta resepti tai lisää oma resepti")
        print("")
    
    reseptilista = ["makaronilaatikko","pinaattiletut","bolognese"]
    if resepti not in reseptilista:
        data =omadata

    if resepti == "oma":
        omataineet = []
        omatyksikot = []
        omatmaarat = []
        aineyksikot = []
        ainemaarat = []
        kaikki = []
        resepti =(input("Reseptin nimi?: "))
        while True:
            try:
                a = int(input("Monta aineosaa?: "))
                break
            except ValueError:
                print("Määrä tulee antaa lukuna")
                print("")
        for i in range(a):
            print("")
            print(i+1,":"," ", end="")
            omataineet.append(input("Aineosa? : "))
            omatyksikot.append(input("Yksikkö?: "))
            while True:
                try:
                    omatmaarat.append(float(input("Määrä?: ")))
                    break
                except ValueError:
                    print("Määrä tulee antaa lukuna ja desimaalierottimena toimii piste (.)")
                    print("")
       
            print("")
            print("Reseptin nimi :", resepti)
            print("Aineosat:\n", end="")
            
            for i in range(len(omataineet)):
                print(omataineet[i],":",omatmaarat[i],omatyksikot[i],","," ",end="")
            print("")
        for i in range(len(omataineet)):
            aineyksikot.append(omataineet[i])
            aineyksikot.append(omatyksikot[i])
        for i in range(len(omataineet)):
            ainemaarat.append(omataineet[i])
            ainemaarat.append(int(omatmaarat[i]))
        
        omaainemaara = omaresepti(ainemaarat)
        omaaineyksikot = omaresepti(aineyksikot)
        reseptit = {}
        reseptit[resepti] = []
        reseptit[resepti].append(omaainemaara)
        reseptit[resepti+"yksikot"] = []
        reseptit[resepti+"yksikot"].append(omaaineyksikot)
        
        with open("omaresepti.txt","w") as tiedosto:
            json.dump(reseptit,tiedosto)
        with open("omaresepti.txt","r") as tiedosto:
            data = json.load(tiedosto)
            
    maarat = (valinta(resepti,data))
    yksikot = (yksikot(resepti+"yksikot",data))
    aineosat =(index(resepti,aineosat,data))
    print("")
    print("Aineosat:")
    for i in range(len(aineosat)):
        print("-",aineosat[i],":",yksikot[i])
        
    print("")
    
    while True:
        try:
            muutettava = aineosat.index(input("Minkä aineosan suhteen muunnetaan? (kirjoita yksikkömuodossa) :"))
            break
        except ValueError as f:
            print("Aineosaa ei löytynyt kyseisestä reseptistä.")
            print("")
            
    while True:
        try:
            mitta = float(input("Määrä? :"))
            break
        except ValueError:
            print("Määrä tulee antaa lukuna ja desimaalierottimena toimii piste (.)")
            print("")
            
    print("")
    print("Resepti: ",resepti)
    for i in range(len(aineosat)):
        print(aineosat[i], ":", maarat[i]*(mitta/maarat[muutettava]),yksikot[i])
    print("")
   
    a = input("Aloitetaanko alusta ? (kyllä/ei): ")
    if a == "kyllä":
               reseptikone()
    print("")
    print("Kiitos ja näkemiin!")
    exit()
        
reseptikone()


        


        


                
                

