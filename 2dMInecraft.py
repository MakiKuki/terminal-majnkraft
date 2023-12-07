# 2D Minecraft
# 98% napravio Maksim
#definisemo klasu Player
class Player:
    def __init__(self, X, Y, inv, inHand):
        self.posX = X
        self.posY = Y
        self.inventory = inv
        self.equipped = inHand

#funkcija za dodavanje stvari u inventory i prima klasu Player
def addToInv(playerStat):
    playerInv = ["ruka"]
    playerStat.inventory = playerInv
    playerInv.append(input("Unesite koji item zelite da dodate>> "))
    return playerInv

#funkcija za printanje inventorya
def printInv(lst):
    print(*lst, sep="   ")

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
    return inv


#pravimo instancu klase Player koja se zove player(pazi na veliko i malo slovo)
player = Player(X=0, Y=0, inv=[], inHand="")

#printamo sta je equipano(test)
print(player.equipped)
#tvoj zadatak je da napravis if-ove i elif-ove koji pozivaju odgovarajucu funkciju kada igrac unese odgovarajucu komandu
