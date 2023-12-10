import random
# 2D Minecraft
#definisemo klasu Player
print("Dobrodosli u terminal minecraft.Za vise informacija o koriscenju ukucajte pomoc")
resouces = ["kamen","zemlja","drvo","metal","psenica","cvijet","pjesak","tkanina","plastika","zlato","jabuka","ugalj"]
notResouces = ["cekic","mac","kramp","sjekira","lopata"]
bioms = ["livadi","sumi","snjezomi_biomu","okeanu","pustinji","savani","kanjonu"]

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
    "bomba":["barut","metal"]
}

class Player:
    def __init__(self, X, Y, inv, inHand,biome):
        self.posX = X
        self.posY = Y
        self.inventory = inv
        self.equipped = inHand
        self.loc = biome

def biomGenerator(playerStat,bioms):
    biom = random.choice(bioms)
    playerStat.loc = biom

#funkcija za dodavanje stvari u inventory i prima klasu Player
def addToInv(playerStat,res):
    unos = input("Unesite neki od resursa: ")
    if unos == "voda" and playerStat.loc == "okeanu":
        playerStat.inventory.append("voda")

    elif unos == "voda" and not playerStat.loc == "okeanu":
        print("niste u okeanu")

    elif unos in res:
        playerStat.inventory.append(unos)
    else:
        print("resurs nije prepoznat")



def mapa(playerStat,biomList):
    print("X:", playerStat.posX)
    print("Y:", playerStat.posY)

    


#funkcija za printanje i    nventorya
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

    #hello,open the noor


#pravimo instancu klase Player koja se zove player(pazi na veliko i malo slovo)
player = Player(X=0, Y=0, inv=["hand",], inHand="hand",biome="okeanu")

app = True
while app == True:
    unos = input("Unesite komandu{> ")


    if unos == "dodaj":
        addToInv(player,resouces)

    elif unos == "torba":
        printInv(player)

    elif unos == "uzmi":
        equip(player)

    elif unos == "pomjeri":
        move(player)
        biomGenerator(player,bioms)

    elif unos == "izbaci":
        removeFromInv(player)

    elif unos == "napravi":
        craft(player,kraft,notResouces)

    elif unos == "kraj":
        app = False


    elif unos == "mapa":
        mapa(player,bioms)
        print("sada ste u", player.loc)

    elif unos == "pomoc":
        print("Dobrodosli u terminal-minecraft")
        print("Da dodate stvari u torbu koristite 'dodaj' komandu")
        print("Da bi vidjeli sta imate u torbi samo ukucajte 'torba'")
        print("Da bi uzeli item iz torbe u terminal napisite 'uzmi'")
        print("Da bi promjenili lokaciju igraca ukucajte 'pomjeri'")
        print("Da bi izbacili item iz torbe koristite komandu 'izbaci'")
        print("Da bi napravili nesto od resorsa u torbi ukucajte 'napravi'")
        print("Da bi izasli iz igre ukucajte 'kraj'")
    else:
        print("komanda nije validna")
