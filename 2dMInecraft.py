# 2D Minecraft
#definisemo klasu Player
class Player:
    def __init__(self, X, Y, inv, inHand):
        self.posX = X
        self.posY = Y
        self.inventory = inv
        self.equipped = inHand

#funkcija za dodavanje stvari u inventory i prima klasu Player
def addToInv(playerStat):
    playerStat.inventory.append(input("Unesite koji item zelite da dodate>> "))

#funkcija za printanje inventorya
def printInv(playerStat):
    Inventory = playerStat.inventory
    print(*Inventory, sep="   ")

#funkcija koja prima parametar klasu Player i ona stavlja stvari u ruku igraca(equipa)
def equip(playerStat):
    inHand = input("Unesite koji item iz inventory-a da uzmete u ruku(equipate)>> ")
    if inHand in playerStat.inventory:
        playerStat.equipped = inHand
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

def craft(playerStat):
    print("")
    print(*playerStat.inventory,sep = "   ")

    playerStat.inventory.append("something")#ustvari return




        


#pravimo instancu klase Player koja se zove player(pazi na veliko i malo slovo)
player = Player(X=0, Y=0, inv=[], inHand="")

#printamo sta je equipano(test)

#tvoj zadatak je da napravis if-ove i elif-ove koji pozivaju odgovarajucu funkciju kada igrac unese odgovarajucu komandu
craft(player)
###########################################################################################################################################################
###########################################################################################################################################################


