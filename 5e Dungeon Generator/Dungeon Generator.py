import os

from Classes import *

#creates the folders that will hold the room layouts and encounters
os.mkdir("Dungon")
os.mkdir("Dungon/Floor 1")
document = open("Dungon/Floor 1/Floor 1 encounters.txt", 'w')
document.write("Spawn locations are up to the DM. \nEach room on the floor map is numbered corresponding to the number "
               "on the list.\nSome rooms will have conditions it is up to the DM weather or not to tell the players "
               "these exist.\n")

#Array the stores posible rooms 
#Floor(Image location, sides TRBL 1 = open 0 = closed, bool for encounter)
MAPS = [
    Floor("Floor Plans/Shop.jpg", "1111", False),
    Floor("Floor Plans/Room 1.jpg", "1111", True),
    Floor("Floor Plans/Room 2.jpg", "0011", True),
    Floor("Floor Plans/Room 3.jpg", "0001", True),
    Floor("Floor Plans/Room 4.jpg", "0101", True),
    Floor("Floor Plans/Room 5.jpg", "1101", True),
    Floor("Floor Plans/Room 6.jpg", "1010", False)
]

#bool to make sure specific floors don't get generated more than once
shopUsed = False

#TEMP sets special conditions for specific floor plans
MAPS[0].setCondition("This is a shop eventually it will have Items")
MAPS[6].setCondition("This Room is in total Darkness")

#Array holding boss room layouts
BOSSMAPS = [
    Floor("Floor Plans/Boss Rooms/Top Open Boss.jpg", "1000", True),
    Floor("Floor Plans/Boss Rooms/Right Open Boss.jpg", "0100", True),
    Floor("Floor Plans/Boss Rooms/Bot Open Boss.jpg", "0010", True),
    Floor("Floor Plans/Boss Rooms/Left Open Boss.jpg", "0001", True)
]

#player amount and starting level to scale the encounters
pNum = 4  # int(input("How many players are there: "))
pLevel = 1  # int(input("What level are the players: "))

#creats the dungeon a list of rooms and generate the first encounter
dungeon = [Room(MAPS[random.randrange(len(MAPS))], (2880, 2880), 0)]
document.write(str(1) + ": " + str(createMatch(pLevel, pNum)) + '\n')


listNum = 1 #counter for amount of rooms
lastAdd = dungeon[0] #keeps track of last room added

#toggles booleans if a unique room was used
if dungeon[0].floor == MAPS[0]:
    shopUsed = True

#Checks to make sure the room passed through is compatable with the previous room
def check(room2):
    if (lastAdd.top == room2.bottom) and lastAdd.loc[0] != 0 and lastAdd.top != '0':
        return "top"
    elif lastAdd.right == room2.left and lastAdd.loc[1] != 5760 and lastAdd.right != '0':
        return "right"
    elif lastAdd.bottom == room2.top and lastAdd.loc[0] != 5760 and lastAdd.bottom != '0':
        return "bottom"
    elif lastAdd.left == room2.right and lastAdd.loc[1] != 0 and lastAdd.left != '0':
        return "left"
    else:
        return "NA"

#checks no rooms overlap
def spotCheck(loc):
    for index in range(len(dungeon)):
        if dungeon[index].loc[0] == loc[0] and dungeon[index].loc[1] == loc[1]:
            print("rooms overlap")
            return False
    else:
        return True


counter = 0
stepCount = 0


def addRoom():
    global lastAdd, counter, listNum, stepCount, shopUsed
    if shopUsed:
        index = random.randrange(1, len(MAPS))
    else:
        index = random.randrange(len(MAPS))
    placeSide = check(MAPS[index])

    if counter < 5 and stepCount < len(dungeon):
        if placeSide == "top" and spotCheck((lastAdd.loc[0], lastAdd.loc[1] - 960)):
            dungeon.append(Room(MAPS[index], (lastAdd.loc[0], lastAdd.loc[1] - 960), listNum))
            if dungeon[len(dungeon) - 1].boolMon:
                document.write(str(listNum + 1) + ": " + str(createMatch(pLevel, pNum)) + '\n')
            else:
                document.write(str(listNum + 1) + ": " + str(dungeon[len(dungeon) - 1].condition) + '\n')
            dungeon[(len(dungeon) - 1)].changeSide('b')
            if dungeon[len(dungeon) - 1].loc[1] == 0:
                dungeon[len(dungeon) - 1].changeSide('t')

        elif placeSide == "right" and spotCheck((lastAdd.loc[0] + 960, lastAdd.loc[1])):
            dungeon.append(Room(MAPS[index], (lastAdd.loc[0] + 960, lastAdd.loc[1]), listNum))
            if dungeon[len(dungeon) - 1].boolMon:
                document.write(str(listNum + 1) + ": " + str(createMatch(pLevel, pNum)) + '\n')
            else:
                document.write(str(listNum + 1) + ": " + str(dungeon[len(dungeon) - 1].condition) + '\n')
            dungeon[(len(dungeon) - 1)].changeSide('l')
            if dungeon[len(dungeon) - 1].loc[0] == 5760:
                dungeon[len(dungeon) - 1].changeSide('r')

        elif placeSide == "bottom" and spotCheck((lastAdd.loc[0], lastAdd.loc[1] + 960)):

            dungeon.append(Room(MAPS[index], (lastAdd.loc[0], lastAdd.loc[1] + 960), listNum))
            if dungeon[len(dungeon) - 1].boolMon:
                document.write(str(listNum + 1) + ": " + str(createMatch(pLevel, pNum)) + '\n')
            else:
                document.write(str(listNum + 1) + ": " + str(dungeon[len(dungeon) - 1].condition) + '\n')
            dungeon[(len(dungeon) - 1)].changeSide('t')
            if dungeon[len(dungeon) - 1].loc[1] == 5760:
                dungeon[len(dungeon) - 1].changeSide('b')

        elif placeSide == "left" and spotCheck((lastAdd.loc[0] - 960, lastAdd.loc[1])):
            dungeon.append(Room(MAPS[index], (lastAdd.loc[0] - 960, lastAdd.loc[1]), listNum))
            if dungeon[len(dungeon) - 1].boolMon:
                document.write(str(listNum + 1) + ": " + str(createMatch(pLevel, pNum)) + '\n')
            else:
                document.write(str(listNum + 1) + ": " + str(dungeon[len(dungeon) - 1].condition) + '\n')
            dungeon[(len(dungeon) - 1)].changeSide('r')
            if dungeon[len(dungeon) - 1].loc[0] == 0:
                dungeon[len(dungeon) - 1].changeSide('l')

        else:
            counter += 1
            if counter >= 5:
                print("Room step back")
                if stepCount == 0:
                    lastAdd = dungeon[listNum - 2]
                else:
                    lastAdd = dungeon[listNum - (stepCount + 2)]
                counter = 0
                stepCount += 1
            addRoom()
            return None

        lastAdd = dungeon[listNum]
        listNum += 1
        counter = 0
        stepCount = 0

        if lastAdd.floor == MAPS[0]:
            shopUsed = True


def addBoss():
    global counter, stepCount, lastAdd

    for index in range(len(BOSSMAPS)):

        if check(BOSSMAPS[index]) != "NA":

            if check(BOSSMAPS[index]) == "top" and spotCheck((lastAdd.loc[0], lastAdd.loc[1] - 960)):
                dungeon.append(Room(BOSSMAPS[index], (lastAdd.loc[0], lastAdd.loc[1] - 960), listNum))
                if dungeon[len(dungeon) - 1].boolMon:
                    document.write("Boss: " + str(findBoss(pLevel, pNum)) + '\n')
                else:
                    document.write(str(listNum + 1) + ": " + str(dungeon[len(dungeon) - 1].condition) + '\n')
                dungeon[(len(dungeon) - 1)].changeSide('b')
                if dungeon[len(dungeon) - 1].loc[1] == 0:
                    dungeon[len(dungeon) - 1].changeSide('t')
                return None

            elif check(BOSSMAPS[index]) == "right" and spotCheck((lastAdd.loc[0] + 960, lastAdd.loc[1])):
                dungeon.append(Room(BOSSMAPS[index], (lastAdd.loc[0] + 960, lastAdd.loc[1]), listNum))
                if dungeon[len(dungeon) - 1].boolMon:
                    document.write("Boss: " + str(findBoss(pLevel, pNum)) + '\n')
                else:
                    document.write(str(listNum + 1) + ": " + str(dungeon[len(dungeon) - 1].condition) + '\n')
                dungeon[(len(dungeon) - 1)].changeSide('l')
                if dungeon[len(dungeon) - 1].loc[0] == 5760:
                    dungeon[len(dungeon) - 1].changeSide('r')
                return None

            elif check(BOSSMAPS[index]) == "bottom" and spotCheck((lastAdd.loc[0], lastAdd.loc[1] + 960)):
                dungeon.append(Room(BOSSMAPS[index], (lastAdd.loc[0], lastAdd.loc[1] + 960), listNum))
                if dungeon[len(dungeon) - 1].boolMon:
                    document.write("Boss: " + str(findBoss(pLevel, pNum)) + '\n')
                else:
                    document.write(str(listNum + 1) + ": " + str(dungeon[len(dungeon) - 1].condition) + '\n')
                dungeon[(len(dungeon) - 1)].changeSide('t')
                if dungeon[len(dungeon) - 1].loc[1] == 5760:
                    dungeon[len(dungeon) - 1].changeSide('b')
                return None

            elif check(BOSSMAPS[index]) == "left" and spotCheck((lastAdd.loc[0] - 960, lastAdd.loc[1])):
                dungeon.append(Room(BOSSMAPS[index], (lastAdd.loc[0] - 960, lastAdd.loc[1]), listNum))
                if dungeon[len(dungeon) - 1].boolMon:
                    document.write("Boss: " + str(findBoss(pLevel, pNum)) + '\n')
                else:
                    document.write(str(listNum + 1) + ": " + str(dungeon[len(dungeon) - 1].condition) + '\n')
                dungeon[(len(dungeon) - 1)].changeSide('r')
                if dungeon[len(dungeon) - 1].loc[0] == 0:
                    dungeon[len(dungeon) - 1].changeSide('l')
                return None


    print("Room step back")
    if stepCount == 0:
        lastAdd = dungeon[listNum - 2]
        stepCount += 1
    else:
        lastAdd = dungeon[listNum - (stepCount + 2)]
        stepCount += 1
    addBoss()
    return None


def createDungon(flooramount):
    global document, pLevel, lastAdd, listNum, shopUsed,counter, stepCount
    floorNum = 1
    for floors in range(flooramount):
        for i in range(5):
            addRoom()
        addBoss()
        complete = Image.new('RGB', (960 * 7, 960 * 7), (250, 250, 250))
        for encounter in dungeon:
            complete.paste(encounter.floorImg, encounter.loc)
        complete = complete.save("Dungon/Floor " + str(floorNum) + "/Floor " + str(floorNum) + ".jpg")
        document.close()

        if floors != range(flooramount)[len(range(flooramount))-1]:
            floorNum += 1
            pLevel += 1
            os.mkdir("Dungon/Floor " + str(floorNum))
            document = open("Dungon/Floor " + str(floorNum) + "/Floor " + str(floorNum) + " encounters.txt", 'w')
            shopUsed = False
            dungeon.clear()
            dungeon.append(Room(MAPS[random.randrange(len(MAPS))], (2880, 2880), 0))
            document.write(str(1) + ": " + str(createMatch(pLevel, pNum)) + '\n')

        listNum = 1
        lastAdd = dungeon[0]
        counter = 0
        stepCount = 0

        if dungeon[0].floor == MAPS[0]:
            shopUsed = True

    #complete.show()
    #os.startfile("Encounter List.txt")

createDungon(5)
