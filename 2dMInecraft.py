# 2D Minecraft
#definisemo klasu Player
print("Dobrodosli u terminal minecraft.Za vise informacija o koriscenju ukucajte pomoc")
resouces = ["kamen","zemlja","drvo","metal","psenica","cvijet","pjesak"]

kraft = {
    "cekic": ["metal","drvo"],
    "mac": ["cekic","metal","drvo"],
    "kramp": ["cekic","metal","drvo"],
    "sjekira":["mac","cekic","metal","drvo"],
    "lopata":["cekic",],
    "krevet": ["drvo","cvijet"],
    "brasno": ["psenica"],
    "hljeb": ["brasno"]

}

class Player:
    def __init__(self, X, Y, inv, inHand):
        self.posX: X
        self.posY = Y
        self.inventory = inv
        self.equipped = inHand

#funkcija za dodavanje stvari u inventory i prima klasu Player
def addToInv(playerStat,res):

    unos = input("Unesite koji item zelite da dodate>> ")
    if unos in res:

        playerStat.inventory.append(unos)
        print(unos,'je sad u vasem inventoriu')
    else:
        print("resors nepoznat")

#funkcija za printanje inventorya
def printInv(playerStat):
    Inventory = playerStat.inventory
    print(*Inventory, sep="   ")

#funkcija koja prima parametar klasu Player i ona stavlja stvari u ruku igraca(equipa)
def equip(playerStat):
    inHand = input("Unesite koji item iz inventory-a da uzmete u ruku(equipate)>> ")
    if inHand in playerStat.inventory:
        playerStat.equipped = inHand
        #hello hi an Tshus
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

def craft(playerStat, kraf):
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
        playerStat.inventory.remove(item)

    playerStat.inventory.append(unos)

    print("Uspjesno ste kraftali", unos)

    #hello,open the noor


#pravimo instancu klase Player koja se zove player(pazi na veliko i malo slovo)
player = Player(X=0, Y=0, inv=["hand",], inHand="hand")

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

    elif unos == "izbaci":
        removeFromInv(player)

    elif unos == "napravi":
        craft(player,kraft)

    elif unos == "kraj":
        app = False

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