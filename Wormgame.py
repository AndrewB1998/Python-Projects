kenttä = ["-","-","-","-","b","-","-","-","x","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
kenttämatriisi = [kenttä[i:i+5] for i in range(0,len(kenttä),5)]
for l in kenttämatriisi:
    print(*l)



    
        
def vuoroliikkuminen(kenttä,kenttämatriisi):
    while 3>2:
        
    
        
        valinta = input("""
    w = ylös
    s = alas
    a = vasen
    d = oikea
    """)
        
        valintaalas = "s"
        valintaylös = "w"
        valintavasen = "a"
        valintaoikea = "d"
        
        if valinta == "w":
            valintametodi(kenttä,5)
        
        if valinta == "s":
            valintametodi(kenttä,-5)
        
        if valinta == "a":
            valintametodi(kenttä,1)
        
        if valinta == "d":
            valintametodi(kenttä,-1)
        
        
def valintametodi(kenttä,a):
        index = kenttä.index("x")
        kenttä[index-a] = "x"
        if "b" not in kenttä:
            kenttä[index] = "o"
            kenttä[index+a] = "-"
            
            kenttämatriisi = [kenttä[i:i+5] for i in range(0,len(kenttä),5)]
            for l in kenttämatriisi:
                print(*l)
            
        else:
            kenttä[index] = "-"
            kenttämatriisi = [kenttä[i:i+5] for i in range(0,len(kenttä),5)]
            for l in kenttämatriisi:
                print(*l)
            
            
            

vuoroliikkuminen(kenttä,kenttämatriisi)
                