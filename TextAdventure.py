"""
Rahul Shah
Text Adventure game
TextAdventure.py
Period 3

Explores poverty in a first person POV

11/30/15
"""

print("WELCOME TO UGANDA SIMULATOR 2K15")

#money represents the amount of money you have to spend

money = 1000.0

print("You are a poor single parent with 2 children, one that is 13 and one that is 17.")


#name of the player
name = input("What is your name?")

print(name , ", you live in a small village, where everyone knows everyone. Water and food are scarce")

#Initial choice, branches off from here
answer = input(" The water pump has broken and your child has fallen sick. you can 1. go in search of water, or 2. stay and try to treat your child or 3. Take your child with you?")

if(answer == "1"):
    print("You start the long trip to the water hole with a jub on your head. The sweltering sun burns your back")
    print("Along the way you meet a kid, no older than 18, with a gun strapped to his back lying on the ground in pain. He is covered in sweat.")
    #mercy represents the player's empathy toward the kid
    mercy = input("Do you 1, wake him up or 2, let him be?")
    if(int(mercy) == 1):
        print("You wake him up and ask him what is wrong. He tells you he is thirsty.")
        #represents the player's actions toward the kid
        friend = input("Do you 1. take him with you or 2. tell him the village pump is broken and there is no water?")
        if(int(friend) == 1):
            print("You and the boy walk to the water hole and collect water. He thanks you profusely and leaves to his village. You return to your village")
        else:
            print("You tell him you don't have water and proceed to the water hole. When you return, he is gone.")
        print("You return to the village and bring the water to your hut. You see soldiers from the neighboring village")
        print("They are here to take your food and water.")
        if(int(friend) == 1):
            print("But the young boy you met steps up to the chief and tells him that you saved his life. The villages trade some water for medicine.")
            print("Your child survives because of the medicine, but the village still has no water pump")
        else:
            print("The young boy you saw tells his chief 'They said they had no water to spare, they lied to us.' They sack the town and take guns and food, water, and medicine.")
            #bribe is a double representing how much the player gives for bribe
            bribe = input("Do you want to pay the village chief to spare you?")
            if(bribe.lower() == "yes"):
                print("You give him 700 dollars")
            else:
                print("They take the food and water from the village. Your child dies from lack of medicine, and the village slowly dies out from lack of water")
    else:
        print("You let him be and continue on your journey. You get to the water hole and when you return, the young boy is dead.")
        print("You get back to the village to see it ransacked and destroyed. There is no food but you have brought the water. Your child dies, but your family survives for a week")
elif(answer == "2"):
    print("You take the medicine and tend to your child. They survive but the village is getting low on food.")
    print("A neighboring village arrives, armed with guns. They ask you for a trade. You can give them money for food or medicine for food.")
    #trade represents whether or not the player wants to trade
    trade = input("Do you pay them or keep your money for later? Yes or no")
    if(trade.lower() == "yes"):
        #bribe is a double representing how much the player gives for bribe
        bribe = input("How much do you bribe them?")
        #if the bribe is too little, they kill you
        if(float(bribe) >= 700.0):
            print("They accept and let you go. You live but have no money to go anywhere. You stay at the burnt village.")
        else:
            print("They are offended at your offer and burn your house and village. Your child dies and you are left homeless.")
    else:
        print("You keep the money but they burn your house. You manage to buy a bus ticket to a UN Aid station.")
              
else:
    #child is an int representing their choice on what to do
    child = input("Your child dies on the way to the water hole. You can 1. Go back or 2. bury her here?")
    if(int(child) == 1):
        print("You go back to bury her at the village. It is too dark when you get back to get water and some village members don't survive the night")
    else:
        print("You bury here on the road and continue to get water, but the water is infected by your dirty clothes and your village gets fatally sick.")
