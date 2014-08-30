import random

def choosePath(numberOfPaths):
    choice = 0
    while choice < 1 or choice > numberOfPaths:
        print('1 to ' + str(numberOfPaths) + '> ', end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
            choice = 0
        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
            choice = int(choice)
    print()
    return choice

def pause():
    print('Press enter to continue.')
    input()

def intro():
    print('You have ventured to the realm of dragons, and have finally arrived at the Dragon Cave.')
    print('With your trusty sword at your side and trust backpack on your back, you look upon the fearsome entrance to the cave.')
    print()
    print('Read carefully. The adventure changes each time you play.')
    print('Treasure or certain death await!')
    print()
    pause()
    front()

def front():
    print('You are standing in front of the entrance of the cave.')
    if skulls == 'present':
        print('There are a bunch of human skulls and bones lying around.')
    if skulls == 'absent':
        print('There is a sign here that reads, "Welcome, visitors!"')
    print()
    print('What will you do?')
    print('  1 Go into the cave.')
    print('  2 Climb on top of the cave.')
    path = choosePath(2)
    if path == 1:
        insideOfCave()
    if path == 2:
        topOfCave()

def topOfCave():
    print('After climbing up, you are standing on top of the cave.')
    print('There is a small hole that seems to be a chimney nearby.')
    if dragonLocation == 'upper':
        print('There is a lot of smoke coming out of the hole.')
    print()
    print('What will you do?')
    print('  1 Climb down the hole.')
    print('  2 Climb back down to the front entrance.')
    path = choosePath(2)
    if path == 1:
        goDownChimney()
    if path == 2:
        front()

def insideOfCave():
    print('You are inside front chamber of the cave. You can see the exit of the cave which would take you outside.')
    print('There are two paths that lead deeper into the cave, one that goes up and the other that goes down.')
    print()
    print('What will you do?')
    print('  1 Go outside of the cave.')
    print('  2 Take the upper path deeper into the cave.')
    print('  3 Take the lower path deeper into the cave.')
    path = choosePath(3)
    if path == 1:
        front()
    if path == 2:
        upperArea()
    if path == 3:
        lowerArea()

def goDownChimney():
    if dragonLocation == 'upper':
        print('You climb down into the smokey chimney. The smoke is really thick!... (press enter)')
        input()
        print('The smoke keeps getting thicker. It is getting hard to breathe... (press enter)')
        input()
        print('You have become lost in the smoke, and start coughing. You cannot get any air!... (press enter)')
        input()
        print('ACK! You have suffocated to death! It was kind of dumb to climb into that smokey chimney.')
        return
    if dragonLocation == 'lower':
        print('You climb down the chimney. It seems to lead you somewhere inside the cave.')
        upperArea()

def upperArea():
    print('You are standing in a chamber near the top of the cave. There is a rope ladder to a chimney hole in the ceiling that leads outside.')
    if dragonLocation == 'upper':
        print('The dragon is standing in the chamber! Smoke comes out of his nostrils and floats up and out the hole in the ceiling.')
        pause()
        faceDragon()
    if dragonLocation == 'lower':
        print()
        print('What will you do?')
        print('  1 Climb up and out of the hole.')
        print('  2 Go down to the front of the cave.')
        path = choosePath(2)
        if path == 1:
            topOfCave()
        if path == 2:
            insideOfCave()


def lowerArea():
    print('You are in the lower chamber of the cave. There is a path leading back to the front of the cave.')
    print('This chamber is very large, and there is an underground lake in the chamber. The water is dark and')
    print('murky. You cannot tell how deep it is or what may be in it. In the middle of the lake, you can barely')
    print('see a small island and something on it that is shiny.')
    print()
    if rock == 'present':
        print('There is a large rock near the shore.')
        print('There is a creaky old boat on the shore.')
    if rock == 'sunk':
        print('There is a submerged boat at the bottom of the water near the shore.')
    if rock == 'holding':
        print('There is a creaky old boat on the shore.')
    if rock == 'boat':
        print('There is a creaky old boat on the shore with a large rock in it.')
    print()
    print('What will you do?')
    print('  1 Go to back to the front of the cave.')
    print('  2 Swim the lake to the island.')
    print('  3 Take the creaky old boat to the island.')
    if rock == 'present':
        print('  4 Pick up the large rock.')
    if rock == 'holding':
        print('  4 Put the large rock in the boat.')
    print()
    path = choosePath(4)
    if path == 1:
        front()
        return
    if path == 2:
        swim()
        return
    if path == 3 and rock == 'sunk':
        print('That boat does not look like it is going anywhere.')
        print()
        pause()
        lowerArea()
        return
    if path == 3 and rock != 'sunk':
        rideBoat()
        return
    if path == 4 and rock == 'present':
        takeRock()
        return
    if path == 4 and rock == 'holding':
        putRockInBoat()
        return

def takeRock():
    global rock
    print('You pick up the large rock and put it in your trusty backpack. Ooof! It sure is heavy.')
    print()
    pause()
    rock = 'holding'
    lowerArea()

def putRockInBoat():
    global rock
    print('You set the large rock down in the creaky old boat. The boat rocks from side to side, no pun intended.')
    print()
    pause()
    if boat == 'sinks':
        print('The creaky old boat begins to sink under the weight of the rock!')
        print('Whew! It is a good thing you did not try to take that boat to the island.')
        print()
        rock = 'sunk'
        pause()
        lowerArea()
        return
    if boat == 'floats':
        print('The creaky old boat seems to be holding up under the weight of the rock.')
        print()
        rock = 'boat'
        pause()
        lowerArea()
        return

def swim():
    print('You dive into the water. Yipes! It is icy cold!')
    pause()
    if rock == 'holding':
        print('You begin to swim to the island, but the heavy rock you are holding begins to drag you down!... (press enter)')
        input()
        print('ACK! You cannot get the straps off of your backpack!... (press enter)')
        input()
        print('You begin to drown in the murky, dark waters of the underground lake... (press enter)')
        input()
        print('You have drowned! It was kind of dumb to swim the lake with that heavy rock in your backpack.')
        pause()
        return
    if rock != 'holding':
        print('You begin to swim to the island. The island is further away than you thought... (press enter)')
        input()
        print('You are getting tired from all that swiming. You are not sure you can make it... (press enter)')
        input()
        print('You finally get to the shore of the island. Whew! You do not think it is a good idea to try that swim again!')
        pause()
        island()

def rideBoat():
    print('You get into the creaky old boat and begin to row towards the island... (press enter)')
    input()
    print('Half way to the island, you notice that the boat has a small leak!... (press enter)')
    input()
    print('You row faster and faster as the boat slowly begins to sink.... (press enter)')
    input()

    if boat == 'sinks':
        print('The boat is sinking, and your shoe is stuck to some gum on the bottom of the boat!... (press enter)')
        input()
        print('You try to get your shoe off, but not before your head sinks under the murky water... (press enter)')
        input()
        print('What a dumb way to die. Your adventuring skills were no match for the gum. You have died.')
        pause()
        return
    if boat == 'floats':
        print('The boat sinks, but it floated long enough for you to get close to the shore of the island. After a short swim in the icey waters, you climb onto the island.')
        pause()
        island()
        return


def island():
    print('You are standing on the island in the middle of the underground lake. The shiny glint comes from a large pile of gold and jewels!')
    print('You see there is a rope ladder from the ceiling above the island.')
    pause()
    if dragonLocation == 'upper':
        print('You start putting as much treasure as your backpack can hold.')
        print('You climb the rope ladder, and you see that it leads to a hole in the ceiling that goes outside of the cave.')
        print()
        print('You have escaped from the Dragon Cave with the treasure! Congratulations! You have won the game!')
        pause()
        return
    if dragonLocation == 'lower':
        print('But in front of the treasure is the dragon!')
        pause()
        faceDragon()
        return

def faceDragon():
    print()
    print('The dragon is huge! He stands ten feet tall, and has tough green scales and giant claws.')
    print('His leathery wings are folded back over his massive body, and he smiles at you with giant teeth as whisps of smoke come out of his nostrils.')
    pause()
    print('Your trusty sword is at your side, but the dragon is so scary you think you might soil your trusty pants.')
    print()
    print('The dragon smiles at you, and then speaks...')
    pause()
    print()
    print('"Welcome adventurer. You have come a long way to my cave. Seeking treasure and fortune, are you? Well, I have plenty of it myself."')
    pause()
    print()
    print('"All this gold and jewels is cluttering up my place, and I would like to get rid of it. Why not trade me that fancy sword for as much treasure as you can put into your backpack?"')
    print('"You can climb this rope ladder to exit the cave. You can trust me. I do not want to eat you. I am a friendly vegetarian dragon. What do you say?"')
    print()
    print('What will you do?')
    print('  1 Trust the dragon, and give him your sword in exchange for treasure.')
    print('  2 Attack the dragon with your trusty sword.')
    path = choosePath(2)
    if path == 1:
        print()
        print('You hand over your trusty sword to the dragon. With all that treasure, you could buy a hundred trusty swords!... (press enter)')
        input()
        print('The dragon takes the sword and places it on a rack high on the wall, out of your reach... (press enter)')
        input()
        print('He turns to you and smiles. This dragon sure does smile a lot... (press enter)')
        input()
        print('The dragon begins to open his mouth... (press enter)')
        input()
        print()
        if skulls == 'present':
            print('Giant waves of flame come from the dragons mouth! You are incinerated instantly!')
            print()
            print('The dragon pours barbecue sauce on your well-done corpse. Guess he was\'nt a vegetarian after all.')
            print('After gnawing the meat from your skeleton, he tosses your skull and bones outside the front of his cave.')
            print()
            print('You have died.')
            pause()
            return
        if skulls == 'absent':
            print('"Thanks a lot!", the dragon says. "I have started a trusty sword collecting hobby, and yours is the first!"')
            print('"Take as much treasure as you want!"')
            print()
            print('You stuff as much gold and jewels as your trusty backpack can carry, and climb the rope ladder up to a hole in the ceiling that leads outside.')
            print('The dragon waves goodbye as you leave. You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
            print()
            pause()
            return
    if path == 2:
        print()
        print('You are no fool. You pretend to hand over your sword... (press enter)')
        input()
        print('But at the last minute, you swing it at the dragon\'s neck!... (press enter)')
        input()
        if skulls == 'present':
            print('In one quick swipe, you cut off the dragon\'s head!')
            pause()
            print()
            print('With the dragon slayed, you stuff as much gold and jewels into your trusty backpack as it can hold.')
            print('The rope ladder leads up to a hole in the ceiling that goes outside of the cave.')
            print('You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
            print()
            pause()
            return
        if skulls == 'absent':
            print('But the dragon dodges your blade!')
            pause()
            print('"Fiend!", the dragon shouts. He is really angry at you, and breathes a wave of flame onto you.')
            print('You are incinerated instantly!')
            pause()
            print('The dragon pours barbecue sauce on your well-done corpse, and then wraps you in foil and puts you in his refrigerator.')
            print('It is a little known fact that dragons also have refrigerators in their caves, along with gold and jewels.')
            pause()
            print('The dragon doesn\'t eat you, because he is a vegetarian after all. But he will bring you to the next dragon pot luck dinner.')
            pause()
            print()
            print('You have died.')
            return

while True:
    # Randomly generate the game variables
    if random.randint(1,2) == 1:
        dragonLocation = 'upper'
    else:
        dragonLocation = 'lower'

    if random.randint(1,2) == 1:
        skulls = 'present'
    else:
        skulls = 'absent'

    if random.randint(1,2) == 1:
        boat = 'sinks'
    else:
        boat = 'floats'

    rock = 'present'

    # Start the game
    intro()

    print()
    print('Would you like to play again? Y/N')
    playAgain = input()
    if playAgain == 'Y' or playAgain == 'y':
        continue
    if playAgain == 'N' or playAgain == 'n':
        break
    break