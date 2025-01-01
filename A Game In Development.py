print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("""     Welcome to the Enchanted Island!
Your mission is to find the Enchanted treasure.""")
print("----------------------------------------------")

swim_or_wait = input("""you have come to a beautiful enchanted lake. There seems to be a fate glowing light just barley enough so that you can make it out to be, 
On what seems to be an island just across this lake. 
                                 Type [Swim] to swim across or type [Wait] to wait for a magic boat. 
                                                                    """)
if swim_or_wait == "Wait" or swim_or_wait.lower() == "wait":
    left_or_right = input("""You wait for this boat that takes you over to this weirdly but soothing gravitating island.
You step off this boat and what lies ahead are 2 paths, One that goes left and one that goes right What will you choose? 
                                        Type [Left] or [Right] 
                                                    """)

    if left_or_right == "Left" or left_or_right.lower() == "left":
        doors = input("""You go left out of the two paths while you are walking on this path you notice the path is getting more narrow, more claustrophobic,
                more dark... You wonder if you are gonna ever get to the end of this path. while wondering this you also wonder to yourself
                was this the right choice? all of the sudden you see some light 'a opening' you think to yourself you approach the opening a break in the distance a glow so bright it almost blinds you!
                soon your eyes adjust to the glowing light you are able to see again but are greeted by 3 glowing doors each one unique one glowing red, one blue, and the other yellow...
                you feel like you should open one but what one?!
                                                       type: [Red] [Blue] or [Yellow]
                                                                         """)
        if doors == "Red" or doors.lower() == "Red":
            print("""You open the Red Door and end up getting burned by a fire as hot as the sun! 
                        GAME OVER!""")
        elif doors == "Blue" or doors.lower() == "blue":
            print("""You open the Blue Door and out runs 3 super fast beast that tear you apart!
                        GAME OVER!""")
        elif doors == "Yellow" or doors.lower() == "yellow":
            print("""You open the Yellow Door to find a glowing beautiful chest!
                    CONGRATS YOU WIN!!!!""")
        else:
            print("You have Typed the wrong INPUTS!")

    elif left_or_right == "Right" or left_or_right.lower() == "right":
        print("""You walk into a trap of spikes covered by leaves and Died!
                                       GAME OVER!""")

    else:
        print("You have Typed the wrong INPUTS!")


elif swim_or_wait == "Swim" or swim_or_wait.lower() == "swim":
     print("""YOU HAVE DROWNED! 
   GAME OVER!""")

else:
    print("You have Typed the wrong INPUTS! TRY AGAIN!")