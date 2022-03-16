#AdventureStory.py
#ICS2O1 Uddam Bhathal
#Feb 21, 2020

# Sources used within adventure story - ie Ascii art, etc. 

import time

def a():
    print("     _                _ ")
    print("    | |              | |")
    print("  __| | ___  __ _  __| |")
    print(" / _` |/ _ \/ _ `|/ _` |") 
    print("| (_| |  __/ (_| | (_| |")
    print(" \__,_|\___|\__,_|\__,_|\n")


def b():
    print("___________.__             ___________           .___")
    print("\__    ___/|  |__   ____   \_   _____/ ____    __| _/")
    print("  |    |   |  |  \_/ __ \   |    __)_ /    \  / __ | ")
    print("  |    |   |   Y  \  ___/   |        \   |  \/ /_/ | ")
    print("  |____|   |___|  /\___  > /_______  /___|  /\____ | ")
    print("                \/     \/          \/     \/      \/ \n")


def c():
    print("/,,,,\_____________/,,,,\\")
    print("|,(  )/,,,,,,,,,,,,,\(  ),|")
    print("\__,,,,___,,,,,___,,,,__/") 
    print("/,,,/(')\,,,/(')\,,,\"")
    print("|,,,,___ _____ ___,,,,|")
    print("|,,,/   \\o_o//   \,,,|")
    print("|,,|       |       |,,|")
    print("|,,|   \__/|\__/   |,,|")
    print("\,,\     \_/     /,,/")
    print("\__\___________/__/\n")


# Introduction

print("Welcome to ULTIMATE LIFE SURVIVAL!\n")
print("This is a game where you will choose your own life story by making careful decisions until the very end!")
time.sleep(2)

# This command delays the time of each print statement displayed in the output by 2 seconds

print("Each and every decision made will impact the outcome of your story!")
time.sleep(2)
print("Your final objective is to stay alive until the end. Here's a tip - try not to die!")
time.sleep(2)
print("The story begins in an unknown world filled with infinite possibilities.")
time.sleep(2)
print("You are a survivor of a plane crash, but you do not remember anything about this incident due to the injuries faced during this tragic event.")
time.sleep(2)
print("Thus, you must survive to find the mystery behind your curious existence.")
time.sleep(2)
print("And so the journey begins...")
time.sleep(2)
start = int(input("Type 1 to begin your adventure. Good luck young survivor!\t"))

if start!=1:
        print("Error, please restart and type 1 this time...")
if start==1:
    print("You are off to a brand new start in a stranded island with no line of help in sight...")
    time.sleep(2)
    print("Not to worry, you have a trusty hatchet with you; however, you don't know how you obtained the weapon or why you ended up on the island in the first place.")
    time.sleep(2)
    print("Look! You see parts of a plane and they seem to lead to something...")
    time.sleep(2)
    print("Currently, you are low on food and seem to be severely dehydrated.")
    time.sleep(2)
    print("You have a choice to either trust your gut and follow the plane crash marks to hopefully find something useful or explore the area and set up camp before the night falls.")
    time.sleep(2)
    print("Choose wisely as a wrong move can jeopardize your life!")
    time.sleep(2)

# Choice 1 asks the user to make a decision between following the plane crash mystery or setting up camp 
    
    a1 = int(input("Type 1 for finding the mystery behind the plane crash or Type 2 for setting up camp\t"))
    if a1==1:
        print("Let's see where this confidence takes you!")
        time.sleep(2)
        print("You gently grasp your sharp hatchet and begin walking off in the distance.")
        time.sleep(2)
        print("After three kilometers of following the plane tracks, you notice a bright red berry bush!")
        time.sleep(2)
        print("Your stomach begins to rumble and your the floor starts to rain with saliva from your mouth.")
        time.sleep(2)
        print("You think to yourself that you can really use those berries as they look to be sweet and juicy from contrast and texture...")
        time.sleep(2)
        print("However, there may be a chance that these berries are poisonous, but you unfortunately see no plane crash in sight and you are extremely exhausted.")
        time.sleep(2)
        print("Unfortunately, you have to decide if you want to eat the lush berries or continue on walking at a slow pace.")
        time.sleep(2)
        print("Choose wisely as a wrong move can jeopardize your life!")
        time.sleep(2)

# Nested if statements are used throughout the story for each separate decision made 
        
        a2 = int(input("Type 1 to choose to risk it all and eat the berries or Type 2 to disregard the bush and face guilt by moving on to finding the mystery behind the plane crash\t"))
        if a2==1:
            print("Overconfidence is a mistake on its own!")
            time.sleep(2)
            print("Consuming the berries makes you feel energetic on its own and you proceed to continue to track the plane.")
            time.sleep(2) 
            print("Eventually, you feel weakened by your senses and your skin turns pale.")
            time.sleep(2)
            print("You see the plane but you tremble to reach its entrance...")
            time.sleep(2)
            print("An immense pain hits your body and you struggle to stay conscious.")
            time.sleep(2)
            print("It turns out that those berries you ate earlier were indeed poisonous and that your body could not remove all the toxins as you consumed almost every berry on the bush.")
            time.sleep(2)
            print("In other words, you binge ate until the very last berry on the bush was gone.")
            time.sleep(2)
            print("And now you will face the consequences.")
            time.sleep(2)
            print("Goodbye young survivor...")
            time.sleep(2)
            print("Your story is one to be remembered in the books.\n")
            time.sleep(2)

# This defines a preset variable which displays Ascii Art
            
            a()
            
            b()
            
            print("Thank you for playing ULTIMATE LIFE SURVIVAL. Please play again and next time, try not to die... :)")
            
        if a2==2:
            print("Great decision!")
            time.sleep(2)
            print("You now proceed to find the mystery behind the plane crash.")
            time.sleep(2)
            print("While following the damaged plane parts, you notice a shift in weather conditions...")
            time.sleep(2)
            print("The temperature oddly begins to turn cold and you see a blizzard is approaching.")
            time.sleep(2)
            print("You have to make an important choice to either continue searching for the plane in the blizzard or quickly look for shelter.\t")
            time.sleep(2)
            
            a3 = int(input("Type 1 to continue searching in the blizzard or Type 2 to find shelter\t"))
            if a3==1:
                print("Overconfidence is a mistake on its own!")
                time.sleep(2)
                print("Venturing through the blizzard makes life extremely difficult as you cannot see anything and you have now become lost in this chaos.")
                time.sleep(2)
                print("Additionally, the blizzard drops temperatures to negative 20 degrees and since you have barely any clothes on, you suddenly collapse on the ground.")
                time.sleep(2)
                print("Life has become very difficult and you have no hope of surviving in the future.")
                time.sleep(2)
                print("You freeze to death and nothing can be done to save your poor soul.")
                time.sleep(2)
                print("Goodbye young survivor...")
                time.sleep(2)
                print("Your story is one to be remembered in the books.\n")
                time.sleep(2)

# This defines a preset variable which displays Ascii Art
                
                a()
            
                b()
            
                print("Thank you for playing ULTIMATE LIFE SURVIVAL. Please play again and next time, try not to die... :)")
                
            if a3==2:
                print("Nice move!")
                time.sleep(1)
                print("You quickly search for shelter near a short hill and come across a cave.")
                time.sleep(2)
                print("You are currently freezing and need to find warmth immediately!")
                time.sleep(2)
                print("Although the cave seems to be warmer than outside, the structure looks poor and the cave seems as it might collapse if additional pressure is added...")
                time.sleep(2)
                print("Choose wisely if you would want to be warm, but face the chances of rocks falling over your head or find a new place to stay warm")
                time.sleep(2)
                
                a4 = int(input("Type 1 to enter cave or Type 2 to find a new place to stay warm.\t"))
                if a4==2:
                    print("Let's test out your luck!")
                    time.sleep(2)
                    print("The chances of finding a safe and warm shelter in this freezing cold are almost one out of 100.")
                    time.sleep(2)
                    print("Don't let luck fool you because you do not find a shelter regardless.")
                    time.sleep(2)
                    print("Instead you pass out in the cold and struggle to keep warm.")
                    time.sleep(2)
                    print("Chances of surviving the cold are slim.")
                    time.sleep(2)
                    print("Unfortunately, you freeze to death and nothing can be done to save your poor soul.")
                    time.sleep(2)
                    print("Goodbye young survivor...")
                    time.sleep(2)
                    print("Your story is one to be remembered in the books.\n")
                    time.sleep(2)

# This defines a preset variable which displays Ascii Art
                    
                    a()
            
                    b()
            
                    print("Thank you for playing ULTIMATE LIFE SURVIVAL. Please play again and next time, try not to die... :)")

                if a4==1:
                    print("Sometimes, taking risks are better than dying off slowly...")
                    time.sleep(2)
                    print("Anyhow, you enter the cave and feel small pebbles hitting your head")
                    time.sleep(2)
                    print("You wonder if you should return back outside or continue wondering in the cave for potential resources...")
                    time.sleep(2)
                    
                    a5 = int(input("Type 1 to rush outside to avoid possible death/injury or type 2 to continue venturing off in the cave\t"))
                    if a5==1:
                        print("Maybe it's better to worry less about the future than the present...")
                        time.sleep(2)
                        print("While rushing out of the cave, a giant boulder hits your head and you experience internal and external bleeding!")
                        time.sleep(2)
                        print("You gasp for air, but your skull has been severely injured by the boulder.")
                        time.sleep(2)
                        print("You begin to cry and all of the memories of rush back to you.")
                        time.sleep(2)
                        print("You begin to realize that a plane crash was the reason of everything.")
                        time.sleep(2)
                        print("All of the memories of your loved ones rush to you")
                        time.sleep(2)
                        print("As the final tear drop runs across your face, your story has now come to an end!")
                        time.sleep(2)
                        print("Goodbye young survivor...")
                        time.sleep(2)
                        print("Your story is one to be remembered in the books.\n")

# This defines a preset variable which displays Ascii Art
                        
                        a()
            
                        b()
            
                        print("Thank you for playing ULTIMATE LIFE SURVIVAL. Please play again and next time, try not to die... :)")

                    if a5==2:
                        print("You have come so far and have made every smart decision to prevent death!")
                        time.sleep(2)
                        print("Your future is bright, filled with love and passion in the air")
                        time.sleep(2)
                        print("Moving forward, you venture deep into the cave.")
                        time.sleep(2)
                        print("What's that! You see an unlocked refrigerator...")
                        time.sleep(2)
                        print("You quickly rush to see what's inside")
                        time.sleep(2)
                        print("No way! You find soda cans and frozen cheese!!!")
                        time.sleep(2)
                        print("You slap yourself to make sure that you are not dreaming, but it turns out that this is indeed the reality of everything.")
                        time.sleep(2)
                        print("You binge eat all of the food and now feel better than ever!")
                        time.sleep(2)
                        print("You question that all of this food must have come from somewhere...but from where and most importantly, from who?!")
                        time.sleep(2)
                        print("You hear loud footsteps of some sort of creature.")
                        time.sleep(2)
                        print("You see humans with black faces; oh wait, they are miners!")
                        time.sleep(2)
                        print("You scream to the other people and they reply by quickly escorting you out of the vicinity.")
                        time.sleep(2)
                        print("No questions asked.")
                        time.sleep(2)
                        print("You soon see a helicopter land with other people inside")
                        time.sleep(2)
                        print("They transport you to a safe place where you later meet your family.")
                        time.sleep(2)
                        print("All of the hard work paid off and life is back as normal.\n\n")
                        time.sleep(2)
                        print("CONGRATULATIONS, you have finally won the game! What? do you want a cookie or something!")
                        time.sleep(2)
                        print("just kidding, you can now brag to your friends about beating this game itself; have fun!")
                        time.sleep(2)
                        print("I hope you enjoyed your adventure with me and as always, try again to see what other choices would have brought you in the end...")
                        time.sleep(2)
                        print("After all, an adventure isn't really a story until conflict is a surprise.")
                        time.sleep(2)
                        print("From Creator:")
                        time.sleep(2)

# This defines a preset variable which displays Ascii Art
                        
                        c()

                        b()

                        print("Thank you for playing ULTIMATE LIFE SURVIVAL. Please play again and next time, try not to die... :)")

    if a1==2:
        print("Let's see where this confidence takes you!")
        time.sleep(2)
        print("You gently grasp your sharp hatchet and begin searching for resources like rocks and logs.")
        time.sleep(2)
        print("Tree by tree, you obtain enough logs and leaves to build a temporary shelter for the night.")
        time.sleep(2)
        print("Though this is the case, you have now entered starvation mode and your body is more likely to catch a disease and die from infection.")
        time.sleep(2)
        print("Not only this, but you are extremely thirsty and must find some type of water!")
        time.sleep(2)
        print("However, you have used up a lot of time in building the camp and now have to make an important decision.")
        time.sleep(2)
        print("You must decide to explore and find food and water or stay at camp hungry and dehydrated.")
        time.sleep(2)
        print("Note: Staying at camp will increase chances of bacterial infection.")
        time.sleep(2)
        
        b1 = int(input("Type 1 to explore for food and water or type 2 to stay at the camp\t"))
        if b1==2:
            print("You seem to be confident in your ability to withstand dehydration and hunger!")
            time.sleep(2)
            print("Sadly, the pain severely increases during the night and you ultimately catch an unfortunate virus!")
            time.sleep(2)
            print("This virus spreads increasingly to the next day...")
            time.sleep(2)
            print("Your head begins to ache rapidly and you cannot withstand this unbearable pain.")
            time.sleep(2)
            print("Luckily you take the easy way out and...")
            time.sleep(2)
            print("You stab yourself with a hatchet and eventually bleed to death.")
            time.sleep(2)
            print("Wrong decisions come with a punishment in retrun!")
            time.sleep(2)
            print("Try again and don't think about it.")
            time.sleep(2)
            print("Goodbye young survivor...")
            time.sleep(2)
            print("Your story is one to be remembered in the books.\n")
            time.sleep(2)

# This defines a preset variable which displays Ascii Art
            
            a()
            
            b()

            print("Thank you for playing ULTIMATE LIFE SURVIVAL. Please play again and next time, try not to die... :)")

        if b1==1:
            print("I question your move, young survivor!")
            time.sleep(2)
            print("Who knows what could have happened if you stayed overnight...")
            time.sleep(2)
            print("Anyways, you proceed to head out to find food and hopefully, clean water.")
            time.sleep(2)
            print("During your painful walk, you see the parts of the plane to increase in size and mass")
            time.sleep(2)
            print("Suddenly, you notice a bright blue lake!")
            time.sleep(2)
            print("You could really use some water as it has been a week without the precious resource itself.")
            time.sleep(2)
            print("Now the question depends on your human instinct.")
            time.sleep(2)
            print("Would you like to head towards the lake and drink up on water or trust in the plane sight to have resources?")
            time.sleep(2)
            
            b2 = int(input("Type 1 to head towards the lake and drink up on water or Type 2 to trust in the plane sight to have resources\t"))
            if b2==1:
                print("Without a week of water, it makes sense that nobody would resist...")
                time.sleep(2)
                print("You proceed to drink the water and your body feels a lot more energized.")
                time.sleep(2)
                print("After drinking up on water, you move out of the lake to find the plane crash site for food of course.")
                time.sleep(2)
                print("In the middle of the walk, you puke out a large E. Coli worm that had been in the water ever since!")
                time.sleep(2)
                print("It turns out that you had never realized in the first place due to your undying thirst you had earlier.")
                time.sleep(2)
                print("Eventually, these worms begin pinching on your inner organs and now you are internally bleeding!")
                time.sleep(2)
                print("Going to the lake was a bad idea after all!")
                time.sleep(2)
                print("Unfortunately, you die from excessive internal bleeding and no hope is to be found.")
                time.sleep(2)
                print("Goodbye young survivor...")   
                time.sleep(2)
                print("Your story is one to be remembered in the books.\n")
                time.sleep(2)

# This defines a preset variable which displays Ascii Art
            
                a()
            
                b()

                print("Thank you for playing ULTIMATE LIFE SURVIVAL. Please play again and next time, try not to die... :)")

            if b2==2:
                print("Smart, but foolish instincts, young survivor!")
                time.sleep(2)
                print("You head out to find hope in the plane crash site for resources and water.")
                time.sleep(2)
                print("After a long walk, you finally see the plane crash site!")
                time.sleep(2)
                print("You proceed to enter the site; however, everything seems to be blown up and gone!")
                time.sleep(2)
                print("All you find are dead bodies scattered in red.")
                time.sleep(2)
                print("Your heart begins to race and collapse!")
                time.sleep(2)
                print("With no food or water in sight, you last for another 12 hours until you pass away...")
                time.sleep(2)
                print("Good bye young survivor...")
                time.sleep(2)
                print("Your story is one to be remembered in the books.\n")
                time.sleep(2)

# This defines a preset variable which displays Ascii Art
            
                a()
            
                b()

                print("Thank you for playing ULTIMATE LIFE SURVIVAL. Please play again and next time, try not to die... :)")
                

