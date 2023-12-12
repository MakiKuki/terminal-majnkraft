
#importujemo random modul
import random

print("Dobrodosli u terminal minecraft.Za vise informacija o koriscenju ukucajte pomoc")


#Definisemo portebne liste
resouces = ["kamen","zemlja","drvo","metal","psenica","cvijet","pjesak","tkanina","zlato","jabuka","ugalj"]
notResouces = ["cekic","mac","kramp","sjekira","lopata"]
bioms = ["livadi","sumi","snjezom_biomu","okeanu","pustinji","savani","kanjonu"]
armour = ['drvena_kapa', 'drvena_majca', 'drvene_cipele', 'metalna_kapa', 'metalna_majca', 'metalne_cipele', 'metalne_hlace', 'zlatna_kapa', 'zlatna_majca', 'zlatne_cipele', 'zlatne_hlace']

head = ['drvena_kapa', 'metalna_kapa', 'zlatna_kapa']
chest = ['drvena_majca', 'metalna_majca', 'zlatna_majca']
legs = ['metalne_hlace', 'zlatne_hlace']
boots = ['drvene_cipele', 'metalne_cipele', 'zlatne_cipele']

livada = ["psenica","cvijet"]
suma = ["drvo","jabuka"]
snjezni_biom = ["drvo","metal"]
okean = ["voda"]
pustinja = ["pjesak","tkanina"]
savana = ["drvo"]
kanjon = ["zlato","pjesak","ugalj"]

#               0      1        2        3       4       5      6
listaBioma = [livada,suma,snjezni_biom,okean,pustinja,savana,kanjon]

#Definisemo dict sa svim receptima i itemima

kraft = {
    "cekic": ["metal","drvo"],
    "mac": ["cekic","metal","drvo"],
    "kramp": ["cekic","metal","drvo"],
    "sjekira":["mac","cekic","metal","drvo"],
    "lopata":["cekic","drvo",],



    "krevet": ["drvo","cvijet"],
    "brasno": ["psenica"],
    "tjesto":["brasno","voda"],
    "hljeb": ["tjesto"],
    "cigla":["kamen","pjesak"],
    "kanta":["metal","cekic","voda"],
    "kanta_vode":["kanta","voda"],


    "zlatna_jabuka":["jabuka","zlato"],
    "barut":["ugalj"],
    "bomba":["barut","metal"],
    "tanjir":["metal"],

    "drvena_kapa":["drvo","tkanina"],
    "drvena_majca":["drvo","drvo","drvo","tkanina"],
    "drvene_cipele":["drvo","drvo","tkanina"],


    "metalna_kapa":["metal","drvena_kapa"],
    "metalna_majca":["metal","metal","metal","drvena_majca"],
    "metalne_cipele":["metal","metal","drvene_cipele"],
    "metalne_hlace":["metal","metal"],

    "zlatna_kapa":["zlato","metalna_kapa"],
    "zlatna_majca":["zlato","zlato","zlato","metalna_majca"],
    "zlatne_cipele":["zlato","zlato","metalne_cipele"],
    "zlatne_hlace":["zlato","zlato","metalne_hlace"]
}




#definisemo klasu Player

class Player:
    def __init__(self, X, Y, inv, inHand, biome, glava, noge, stopala, trup):
        self.posX = X
        self.posY = Y
        self.inventory = inv
        self.equipped = inHand
        self.loc = biome
        self.head = glava
        self.body = trup
        self.legs = noge
        self.feet = stopala

#Ova funkcija generise random biome svaki put kad je pozvana

def biomGenerator(playerStat,bioms):
    biom = random.choice(bioms)
    playerStat.loc = biom

#funkcija za dodavanje stvari u inventory i prima klasu Player
def addToInv(playerStat,listaBioma):
    unos = input("Unesite neki od resursa: ")


    if unos == "voda" and playerStat.loc == "okeanu":
        playerStat.inventory.append("voda")

    elif unos == "voda" and not playerStat.loc == "okeanu":
        print("niste u odgovarajucem biomu")


    elif unos in listaBioma[0] and playerStat.loc == "livadi":
        playerStat.inventory.append(unos)

    elif unos in listaBioma[0] and not playerStat.loc == "livadi":
        print("niste u odgovarajucem biomu")



    elif unos in listaBioma[1] and playerStat.loc == "sumi":
        playerStat.inventory.append(unos)

    elif unos in listaBioma[0] and not playerStat.loc == "sumi":
        print("niste u odgovarajucem biomu")



    elif unos in listaBioma[2] and playerStat.loc == "snjezom_biomu":
        playerStat.inventory.append(unos)

    elif unos in listaBioma[2] and not playerStat.loc == "snjezom_biomu":
        print("niste u odgovarajucem biomu")


    elif unos in listaBioma[4] and playerStat.loc == "pustinji":
        playerStat.inventory.append(unos)

    elif unos in listaBioma[4] and not playerStat.loc == "pustinji":
        print("niste u odgovarajucem biomu")

    elif unos in listaBioma[5] and playerStat.loc == "savani":
        playerStat.inventory.append(unos)

    elif unos in listaBioma[5] and not playerStat.loc == "savani":
        print("niste u odgovarajucem biomu")


    elif unos in listaBioma[6] and playerStat.loc == "kanjonu":
        playerStat.inventory.append(unos)

    elif unos in listaBioma[6] and not playerStat.loc == "kanjonu":
        print("niste u odgovarajucem biomu")





#funkcija koja prima player klasu i ispisuje X i Y poziciju
def mapa(playerStat):
    print("X:", playerStat.posX)
    print("Y:", playerStat.posY)
   


#funkcija za printanje torbe
def printInv(playerStat):
    Inventory = playerStat.inventory
    print(*Inventory, sep="   ")




#funkcija koja prima parametar klasu Player i ona stavlja stvari u ruku igraca(equipa)
def equip(playerStat):
    inHand = input("Unesite koji item iz inventory-a da uzmete u ruku(equipate)>> ")
    if inHand in playerStat.inventory:
        playerStat.equipped = inHand
        #hello hi and Tshus
    else:
        print("Item nemate u inventory-u")
 





#funkcija prima za parametar klasu Player i ona izbacuje stvari iz inventorija
def removeFromInv(playerStat):
    inv = playerStat.inventory
    item = input("unesite ime itema koji zelite da izbacite>> ")
    if item in inv:
        inv.remove(item)
    else:
        print("ovaj item nemate u inventoriu>> ")
    playerStat.inventory = inv






def move(playerStat):
    playerStat.posX = input("Unesite nove X koordinate>> ")
    playerStat.posY = input("Unesite Y koordinate>> ")
    print("Nove pozicije vaseg lika su: X =", playerStat.posX,"Y =",playerStat.posY)



def changeArmor(playerStat,head,chest,boots,legs):
    unos = input("Unesite neki od dijelova oklopa u svojoj torbi: ")


    if unos in head and playerStat.inventory:
        playerStat.head = unos
    elif unos in head and not playerStat.inventory:
        print("Nemate to u torbi")

    elif unos not in head and unos in playerStat.inventory:
        print("Komad oklopa nije odgovarajuci!")



    if unos in chest and playerStat.inventory:
        playerStat.chest = unos
    elif unos in chest and not playerStat.inventory:
        print("Nemate to u torbi")

    elif unos not in chest and unos in playerStat.inventory:
        print("Komad oklopa nije odgovarajuci!")

    
    if unos in boots and playerStat.inventory:
        playerStat.boots = unos
    elif unos in boots and not playerStat.inventory:
        print("Nemate to u torbi")

    elif unos not in boots and unos in playerStat.inventory:
        print("Komad oklopa nije odgovarajuci!")

   
    if unos in legs and playerStat.inventory:
        playerStat.legs = unos
    elif unos in legs and not playerStat.inventory:
        print("Nemate to u torbi")

    elif unos not in legs and unos in playerStat.inventory:
        print("Komad oklopa nije odgovarajuci!")






def craft(playerStat, kraf,Nres):
    kra = list(kraf)
    print(*playerStat.inventory, sep="   ")
    print("Od ovih resursa ce te nesto kraftati")


    unos = input("Koji item hocete da kraftate>> ")

    if unos not in kra:
        print("Item nije prepoznat")
        return 0

    if not set(kraf[unos]).issubset(playerStat.inventory):
        print("Nemate zadane iteme (", *kraf[unos], ")", sep=" ")
        return 0

    for item in kraf[unos]:
        if not item in Nres:
            playerStat.inventory.remove(item)

    playerStat.inventory.append(unos)

    print("Uspjesno ste kraftali", unos)


#pravimo instancu klase Player koja se zove player(pazi na veliko i malo slovo)
player = Player(X=0, Y=0, inv=["hand",], inHand="hand",biome="okeanu",glava = "",noge = "",stopala="", trup = "")









app = True
while app == True:
    unos = input("Unesite komandu{> ")


    if unos == "hp":
        print(100)

    if unos == "dodaj":
        addToInv(player,listaBioma)

    elif unos == "torba":
        printInv(player)

    elif unos == "uzmi":
        equip(player)

    elif unos == "pomjeri":
        move(player)
        biomGenerator(player,bioms)

    elif unos == "oklop":
        changeArmor(player,head,chest,boots,legs)

    elif unos == "izbaci":
        removeFromInv(player)


    elif unos == "oklop_info":
        print(player.head)
        print(player.body)
        print(player.legs)
        print(player.feet)


    elif unos == "napravi":
        craft(player,kraft,notResouces)

    elif unos == "kraj":
        app = False


    elif unos == "mapa":
        mapa(player)
        print("sada ste u", player.loc)

    elif unos == "pomoc":
        print("Dobrodosli u terminal-minecraft")
        print("Da dodate stvari u torbu koristite 'dodaj' komandu")
        print("Da bi vidjeli sta imate u torbi samo ukucajte 'torba'")
        print("Da bi uzeli item iz torbe u terminal napisite 'uzmi'")
        print("Da bi promjenili lokaciju igraca ukucajte 'pomjeri'")
        print("Da bi izbacili item iz torbe koristite komandu 'izbaci'")
        print("Da bi napravili nesto od resorsa u torbi ukucajte 'napravi'")
        print("Ako zelite da saznate koordinate i biom vaseg lika ukucajte 'mapa'")
        print("Da bi izasli iz igre ukucajte 'kraj'")
    else:
        print("komanda nije validna")

   
