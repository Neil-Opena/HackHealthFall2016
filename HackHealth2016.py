#This is an attempt to create a text-based adventure game for HackHealth 2016
#I am a beginner taking CSE 101, (Introduction to Computers) and I am using a YouTube tutorials to assist me with this
#I figured that a text-based game would be appropriate because it is perfect for beginners
#learning Python, such as myself
#It may not be finished in time, but thank you for testing my first full program
#This event definitely helped me gain experience and learn a lot more than I expected!
#Also, I used PyCharm to write the program
def help_function ():
    print ("When playing this game, make sure to capitalize the first letter of the first word. The second word is all lowercase. Ex: 'Look around'  "
           "Some of the responses may not work" )
#My goal was to create a sarcastic and humorous game
def start():
    print('\033[1m' + '\033[91m'
          + '\033[4m' + "HackHealth 2016: Zombie Apocalypse" + '\033[0m'
          )
    print("---a simple text-based adventure---\n")
    print ('\033[1m' + "Type 'Start' to begin:\nType 'Help' for general help" + '\033[0m')
    print ("I suggest looking at the code to look at some of the responses possible")
    print
    prompt_sta ()

def prompt_sta ():
    prompt_0 =input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_0 == 'Start':
            inside_dorm ()
        elif prompt_0 == 'Help':
            help_function ()
            print
            prompt_sta()
        else:
            print ("Can you follow instructions?!?!\n", "Type 'start' to begin:")
            print
            prompt_sta ()
    except ValueError:
        print ("Can you follow instructions?!?!\n", "Type 'start' to begin:")
        print
        prompt_sta ()
def inside_dorm ():
    print ("You are a student of the prestigious 'Stony Brook University'\nYou just woke up\nYou realize that you are alone inside your dorm without anything in your pockets\nWhat do you do?")
    print
    prompt_inside ()
#Once again, this is done with the help of YouTube
def prompt_inside ():
    prompt_1 = input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_1 == 'Go outside':
            print("The door opens slowly, the hallway is dark and musty as fuck.\nThe hallway runs a considerable distance")
            hallway ()

        elif prompt_1 == 'Open door':
            print("The door opens slowly, the hallway is dark and musty as fuck.\nThe hallway runs a considerable distance")
            hallway ()
        elif prompt_1 == 'Go out':
            print("The door opens slowly, the hallway is dark and musty as fuck.\nThe hallway runs a considerable distance")
            hallway ()
        elif prompt_1 == 'Open':
            print ('Open what??')
            print
            prompt_inside ()
        elif prompt_1 == 'Look north':
            print ("There is a closed door in front of you")
            print
            prompt_inside()
        elif prompt_1 == 'Look around':
            print ("There is a table with leftover pizza on the left")
            print ("There is a closed door in front of you")
            print ("Your bed is on the right")
            print ("There is a window behind you, with blood smeared on the outside")
#I apologize for any grammar or spelling mistakes
#Also right now, I dont know how to integrate health to this game...
#so..Im just gonna insert some random health tips and facts for living a healthy life
            print
            prompt_inside ()
        elif prompt_1 == 'Look':
            print ("There is a table with leftover pizza on the left")
            print ("There is a closed door in front of you")
            print ("Your bed is on the right")
            print ("There is a window behind you, with blood smeared on the outside")
            print
            prompt_inside()
        elif prompt_1 == 'Look west':
            print ("There is a table with leftover pizza\nThe pizza is green and moldy with several maggots on top")
            print( '\033[94m' + "\"While an occasional indulgence in commercial pizza is okay,\nif it is a regular feature in your diet,you may want to reconsider your choices.\nPizza can be a healthy option, if you avoid the greasy, refined-flour and processed meat versions.\"")
            print("-http://www.livestrong.com/article/413009-is-eating-pizza-healthy/" + '\033[0m')
            print
            prompt_inside ()
        elif prompt_1 == 'Look left':
#The first of many health tips:
            print ("There is a table with leftover pizza\nThe pizza is green and moldy with several maggots on top")
            print ('\033[94m' + "\"While an occasional indulgence in commercial pizza is okay,\nif it is a regular feature in your diet,you may want to reconsider your choices.\nPizza can be a healthy option, if you avoid the greasy, refined-flour and processed meat versions.\"")
            print ("-http://www.livestrong.com/article/413009-is-eating-pizza-healthy/" + '\033[0m')
            print
            prompt_inside ()
        elif prompt_1 == 'Eat pizza':
            print ("You are extremely stupid and reach in for a bite\n...\n...\n...\nYou immediately feel sick\n...\n...\n...\n...\nYou suddenly stop breathing and die instantaneously\n")
            print ('\033[1m' + '\033[91m' + "Good job, you died without even stepping out of your dorm!!!" + '\033[0m')
            print ("Try again later, when you have a better understanding of general health :)")
            quit()
        elif prompt_1 == 'Look right':
            print ("Your bed is on the right")
            print
            prompt_inside ()
        elif prompt_1 == 'Look east':
            print ("Your bed is on the right")
            print
            prompt_inside ()
        elif prompt_1 == 'Sleep':
            print('\033[94m' + "\"Sleep makes you feel better, but its importance goes way beyond just boosting your mood or banishing under-eye circles. \nAdequate sleep is a key part of a healthy lifestyle, and can benefit your heart, weight, mind, and more.\"")
            print('http://www.health.com/health/gallery/0,,20459221,00.html' + '\033[0m')
            print ("Sleep is good for the body, but now is not the time")
            print
            prompt_inside ()
        elif prompt_1 == 'Look south':
            print ('There is a window with blood smeared on the outside')
            print
            prompt_inside()
        elif prompt_1 == 'Open window':
            print ('The window is locked')
            print
            prompt_inside()
        elif prompt_1 == 'Examine window':
            print ('The window is locked from the outside.\nIt is difficult to see outside because of the blood.')
            print
            prompt_inside()
        elif prompt_1 == 'Look down':
            print ('You see your ashy ass knees. Put some lotion on them knees boi')
            print
            prompt_inside()
        elif prompt_1 == 'Look up':
            print ("You see your crusty ass ceiling. There's nothing really special about it")
            print
            prompt_inside()
#As you can see, I like to implement crude humor in my code
        else:
            print ("I did not have time to write a response to that command...sorry")
            print
            prompt_inside ()

    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_inside()
def hallway ():
    print
    prompt_hallway()
def prompt_hallway():
    prompt_2 = input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_2 == 'Look':
            print ('The hallway runs west to east.\nThere are rooms on the side but all of them seem deserted\nThere is something that looks like a body up ahead to the west')
            print
            prompt_hallway()
        elif prompt_2 == 'Look around':
            print('The hallway runs west to east.\nThere are rooms on the side but all of them seem deserted\nThere is something that looks like a body up ahead to the west')
            print
            prompt_hallway()
        elif prompt_2 == 'Go west':
            hallwayw1 ()
        elif prompt_2 == 'Go east':
            hallwaye1()

        else:
            print ("I did not have time to write a response to that command...sorry")
            print
            prompt_hallway()
    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_hallway()
def hallwaye1():
    print ("You walk across the hallway\nThere is an exit door at the end of the hall\nYou notice that there's some writing on the twin steel exit doors")
    print
    prompt_hallwaye1()
def prompt_hallwaye1():
    prompt_e1 = input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_e1 == "Go east":
            hallwaye2()
        elif prompt_e1 == "Go west":
            print ("You come back west")
            hallway()
        else:
            print("I did not have time to write a response to that command...sorry")
            print
            prompt_hallwaye1()
    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_hallwaye1()
def hallwaye2():
    print ("You approach the twin steel doors")
    print
    prompt_hallwaye2()
def prompt_hallwaye2():
    prompt_e2 = input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_e2 == "Open door":
            print ("You are too weak to open the door")
            print ('\033[94m' + "Maybe if you lifted once in a while,\n you wouldn't be stuck trying to open this door" + '\033[0m')
            print
            prompt_hallwaye2()
        elif prompt_e2 == "Open doors":
            print ("You are too weak to open the door")
            print ('\033[94m' + "Maybe if you lifted once in a while,\n you wouldn't be stuck trying to open this door" + '\033[0m')
            print
            prompt_hallwaye2()
        elif prompt_e2 == "Examine door":
            print ("'SAFE EXIT' is sprayed on the doors")
            print
            prompte_hallwaye2()
        elif prompt_e2 == "Examine doors":
            print ("'SAFE EXIT' is sprayed on the doors")
            print
            prompte_hallwaye2()
        elif prompt_e2 == "Go west":
            print ("You come back west")
            hallwaye1()
        else:
            print("I did not have time to write a response to that command...sorry")
            print
            prompt_hallwaye2()
    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_hallwaye1()
def hallwayw1():
    print('You walk across the hallway\nThe body is getting close')
    print
    prompt_hallwayw1()
def prompt_hallwayw1():
    prompt_w1 = input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_w1 == 'Go west':
            print ('You continue walking west\nYou can tell that it is definitely a body propped on a wall\nIt is extremely close to you\nYou are not sure if it is alive or not')
            hallwayw2()
        elif prompt_w1 == 'Go east':
            print ("You go back east")
            hallway()
        else:
            print ("I did not have time to write a response to that command...sorry")
            print
            prompt_hallwayw1()
    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_hallwayw1()

def hallwayw2():
    print ('The body is an arms reach away')
    print
    prompt_hallwayw2()
def prompt_hallwayw2():
    prompt_w2= input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_w2 == 'Examine body':
            print ('The body is severed in half with its intestines hanging out\nThe head is tilted down, so its difficult to check if its alive without touching it')
            print("You can tell that the person did not live a healthy lifestyle\nIt is extremely large\nIt probably died trying to outrun the zombies and eventually ran out of breath")
            print('\033[94m' + "Cardio is necessary to live a healthy lifestyle. Not only does it help with general health,\n but it could potentially assist you during an apocalypse" + '\033[0m')
            print
            prompt_hallwayw2()
        elif prompt_w2 == 'Examine it':
            print ('The body is severed in half with its intestines hanging out\nThe head is tilted down, so its difficult to check if its alive without touching it')
            print ("You can tell that the person did not live a healthy lifestyle\nIt is extremely large\nIt probably died trying to outrun the zombies and eventually ran out of breath")
            print('\033[94m' + "Cardio is necessary to live a healthy lifestyle. Not only does it help with general health,\n but it could potentially assist you during an apocalypse" + '\033[0m')
            print
            prompt_hallwayw2()
        elif prompt_w2 == 'Examine corpse':
            print ('The body is severed in half with its intestines hanging out\nThe head is tilted down, so its difficult to check if its alive without touching it')
            print("You can tell that the person did not live a healthy lifestyle\nIt is extremely large\nIt probably died trying to outrun the zombies and eventually ran out of breath")
            print('\033[94m' + "Cardio is necessary to live a healthy lifestyle. Not only does it help with general health,\n but it could potentially assist you during an apocalypse" + '\033[0m')
            print
            prompt_hallwayw2()
        elif prompt_w2 == 'Touch body':
            hallwayw2_z()
        elif prompt_w2 == 'Touch it':
            hallwayw2_z()
        elif prompt_w2 == 'Touch corpse':
            hallwayw2_z()
        elif prompt_w2 == 'Kick it':
            hallwayw2_zdead()
        elif prompt_w2 == 'Kill it':
            hallwayw2_zdead()
        elif prompt_w2 == 'Kick body':
            hallwayw2_zdead()
        elif prompt_w2 == 'Kick corpse':
            hallwayw2_zdead()
        elif prompt_w2 == 'Kill corpse':
            hallwayw2_zdead()
        else:
            print("I did not have time to write a response to that command...sorry")
            print
            prompt_hallwayw2()
    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_hallwayw2()
def hallwayw2_z():
    print("The corpse's head tilts forward upon feeling you touch it\nIt is definitely obvious that it is not completely dead yet.\nIt slowly crawls towards you")
    print
    prompt_hallwayw2_z()
def prompt_hallwayw2_z():
    prompt_w2_z = input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_w2_z == 'Kick it':
            hallwayw2_zdead()
        elif prompt_w2_z == 'Kill it':
            hallwayw2_zdead()
        elif prompt_w2_z == 'Kick body':
            hallwayw2_zdead()
        elif prompt_w2_z == 'Kick corpse':
            hallwayw2_zdead()
        elif prompt_w2_z == 'Kill corpse':
            hallwayw2_zdead()
        elif prompt_w2_z == 'Run':
            print ("Really? Why would you run away from a severed corpse that can barely do anything?")
            print
            prompt_hallwayw2_z()
        elif prompt_w2_z == 'Run away':
            print ("Really? Why would you run away from a severed corpse that can barely do anything?")
            print
            prompt_hallwayw2_z()
        else:
            print("You are unable to do that\n...\n...\nYou end up standing still, and the corpse lunges at you...")
            print ("It has a good grip on you\nYou can no longer do anything about it\nIt clenches its mouth on your legs")
            print ("You scream out loud for help, but no one comes\nYou feel the bones crunch\n...\nThe skin tear\n...You die screaming for your life")
            print ('\033[1m' + '\033[91m' + "You died...Good job pal" + '\033[0m')
            quit()
    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_w2_z()
def hallwayw2_zdead():
    print("You kick that piece of shit in the mouth\nYour shoe goes straight through its head, displacing blood everywhere")
    print("You notice that there is a set of keys next to the corpse")
    prompt_hallwayw2_zdead ()
def prompt_hallwayw2_zdead():
    prompt_w2zd=input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_w2zd == 'Take keys':
            hallwayw2_zdead_keys()
        elif prompt_w2zd == 'Grab keys':
            hallwayw2_zdead_keys()
        elif prompt_w2zd == 'Find keys':
            hallwayw2_zdead_keys()
        elif prompt_w2zd == 'Go west':
            print ('You reach the end of the hallway\nThere is a glass door')
            print
            prompt_hallwayw2_zdead()
        elif prompt_w2zd == 'Look':
            print ('There is a door at the end of the hallway')
            print
            prompt_hallwayw2_zdead()
        elif prompt_w2zd== 'Open door':
            print ("The door is padlocked\nPerhaps there's a key nearby")
            print
            prompt_hallwayw2_zdead()
        elif prompt_w2zd== 'Go east':
            print('You pass the body, and go back east')
            print
            prompt_hallwayw1()
        else:
            print ("I did not have time to write a response to that command...sorry")
            print
            prompt_hallwayw2_zdead()
    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_hallwayw2_zdead()
def hallwayw2_zdead_keys ():
    print ("You grab the keys")
    prompt_hallwayw2_zdead_keys()
def prompt_hallwayw2_zdead_keys():
    prompt_w2zd_k=input('\033[1m' + '\033[91m' + "Type a Command:" + '\033[0m')
    try:
        if prompt_w2zd_k =='Go west':
            print('You reach the end of the hallway\nThere is a glassdoor')
            print
            prompt_hallwayw2_zdead_keys()
        elif prompt_w2zd_k == 'Look':
            print ('There is a door at the end of the hallway')
            print
            prompt_hallwayw2_zdead_keys()
        elif prompt_w2zd_k == 'Open door':
            print("You go through the heavy glass doors.\nYou are blinded by the light for a second\nIt takes a while to adjust but you finally realize the situation that you are in..")
            print("So much information is invading your head\n...\n...\n...\n...")
            print("And then you realize...\n...\n...\nYou are fucked...")

            print('\033[1m' + '\033[4m'+ "To be continued...")
            quit()
        elif prompt_w2zd_k == 'Go outside':
            print("You go through the heavy glass doors.\nYou are blinded by the light for a second\nIt takes a while to adjust but you finally realize the situation that you are in..")
            print("So much information is invading your head\n...\n...\n...\n...")
            print("And then you realize...\n...\n...\nYou are fucked...")

            print('\033[1m' + '\033[4m' + "To be continued...")
            quit()
        elif prompt_w2zd_k == 'Use key':
            print("You go through the heavy glass doors.\nYou are blinded by the light for a second\nIt takes a while to adjust but you finally realize the situation that you are in..")
            print("So much information is invading your head\n...\n...\n...\n...")
            print("And then you realize...\n...\n...\nYou are fucked...")

            print('\033[1m' + '\033[4m' + "To be continued...")
            quit()
        else:
            print("I did not have time to write a response to that command...sorry")
            print
            prompt_hallwayw2_zdead_keys()
    except ValueError:
        print("I did not have time to write a response to that command...sorry")
        print
        prompt_hallwayw2_zdead_keys()


#I now realize that creating a text-based game by myself is extremely enjoyable but tiring at the same time
#I was supposed to add more random 'health facts and tips',but I didnt have the time to
start ()
inside_dorm ()
hallway ()
hallwayw1()
hallwayw2()
hallwayw2_zdead ()
hallwaye1()
hallwayw2_z()



