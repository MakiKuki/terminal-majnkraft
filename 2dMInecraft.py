# 2D Minecraft
# 98% napravio Maksim

class Player:
    def __init__(self, X, Y, inv, inHand):
        self.posX = X
        self.posY = Y
        self.inventory = inv
        self.equipped = inHand


def addToInv(playerStat):
    playerInv = ["ruka"]
    playerStat.inventory = playerInv
    playerInv.append(input("Unesite koji item zelite da dodate>> "))
    return playerInv


def printInv(lst):
    print(*lst, sep="   ")


def equip(playerStat):
    inHand = input("Unesite koji item iz inventory-a da uzmete u ruku(equipate)>> ")
    if inHand in playerStat.inventory:
        playerStat.equipped = inHand
    else:
        print("Item nemate u inventory-u")


def removeFromInv(playerStat):
    inv = playerStat.inventory
    return inv


# Create an instance of the Player class
player = Player(X=0, Y=0, inv=[], inHand="")

# Print the equipped item (Note: this will be empty initially)
print(player.equipped)
