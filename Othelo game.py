def Demo1_teht4():
    def merkitse(lauta, paikka, pelaaja):
        uusiLauta = lauta[:paikka-1]
        uusiLauta += pelaaja*3
        uusiLauta += lauta[paikka+2:]
        return uusiLauta
    
    lauta = "-"*int(input("Anna laudan pituus:"))
    vuorot = int(input("Anna vuorojen määrä:"))
    pelaajat = "xo"
    pelaaja = 0
    for vuoro in range(vuorot):
        print(lauta)
        x = input("Pelaaja "+pelaajat[pelaaja]+", mihin laitat?")
        lauta = merkitse(lauta, int(x), pelaajat[pelaaja])
                
        pelaaja = (pelaaja+1) % len(pelaajat)

    voittaja = pelaajat[0]
    for p in pelaajat:
        if laskeMaarat(lauta,p) > laskeMaarat(lauta,voittaja):
            voittaja = p

    print(lauta)
    print("Pelin voiti",voittaja)
    
Demo1_teht4()