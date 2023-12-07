#2d minecraft
#98% napravio Maksim

class player:
    def __init__(self,X,Y,inv,inHand):
        self.posX = X
        self.posY = Y
        self.inventory = inv
        self.equiped = inHand

    




def addToInv(playerStat):
    playerInv = ["ruka"]
    playerStat.inventory  = playerInv
    playerInv.append(input("Unesite koji item zelite da dodate>> "))
    return playerInv



def printInv(list):
    print(*list,sep = "   ")

def equip(playerStat):

    
    inHand = input("Unesite koji item iz inventory-a da uzmete u ruku(equipate)>> ")
    if inHand in playerStat.inventory:
        playerStat.equiped = inHand
    else:
        print("Item nemate u inventory-u")

def removeFromInv(playerStat):

    inv = playerStat.inventory
    return inv

print(player.equiped)
        
        



def move(x,y,playerStat):
    playerStat.posX = x
    playerStat.posX = y



