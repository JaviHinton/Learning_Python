# A fun little project making some silly mad-libs. This project taught me about functions and modules.

import random

def story1():
    print("In a small farm in Dorset, there was a " + str(x) + " called " + str(y) + ".")
    print("The " + str(z) + " were concerned about " + str(x) + "s being in their village.")
    print("This is because a long time ago, a " + str(x) + " came along and " + str(a) + " the " + str(z) + ",")
    print("which left them very nervous.")
    print(str (y) + " decided that it was time to change this outlook, so they put on a " + str(b) + ".")
    print("All of the " + str(z) + " attended and had a great time " + str(c) + "!")
    print("Now the " + str(z) + " and " + str(x) + "s are best of friends. \nThe End.\n")

def story2():
    print("There is an elderly member of the local community called " + str(y) + ".")
    print(str(y) + " was famous in their teens for throwing " + str(b) + "'s that only " + str(z) + " could attend.")
    print("Although loved, these had to stop in the 1940s because a " + str(x) + " kept " + str(c) + " the " + str(z) + "!")
    print("After this, " + str(y) + " felt lost until he met a hipster " + str(x) + " that didn't like " + str(c) + " and they became friends.")
    print("His new " + str(x) + " friend told " + str(y) + " that he " + str(a) + " which " + str(y) + " thought might be interesting.")
    print("After trying it out, " + str(y) + " really enjoyed it, and continues to do it with his " + str(x) + " friend to this day!")
    print("The End.\n")

def story3():
    print(str(y) + " was a dangerous poacher that used to shoot " + str(x) + "s for fun.")
    print("A group of " + str(z) + " were so fed up with his shenanigans that they called together a " + str(b))
    print("to work out how to deal with " + str(y) + ".")
    print("the " + str(z) + " decided that the best way to deal with poachers are to scare them with "+ str(c) + "!")
    print("Early one morning, before " + str(y) + " was awake, the " + str(z) + " snuck their way toward's " + str(y) + "'s house.")
    print("Smashing through the window, the " + str(z) + " started " + str(c) + " in " + str(y) + "'s bedroom, terrifying them.")
    print(str(y) + " never poached again, and to celebrate, all the " + str(z) + " " + str(a) + " eachother!\nThe End.")

print("\n*****************************************")
print("Welcome to Javi Hinton's MadLibs program!")

story_id = random.randint(1,3)

print("Your story has been randomly selected...\n")
print("Playing with story: " + str(story_id))
print("")


#   x = animal (singular)
#   y = name
#   z = profession (plural) - e.g. firemen
#   a = action (past tense)
#   b = event (singular) - e.g. wedding
#   c = action (present) - e.g. dancing

x = input("Please enter an animal (singular): ")
y = input("Please enter a name: ")
z = input("Please enter a profession (plural) - e.g. firemen: ")
a = input("Please enter an action (past tense): ")
b = input("Please enter an event (singular) - e.g. wedding: ")
c = input("Please enter an action (present) - e.g. dancing: ")

print("**************************************")
print("\n\nYour story has been generated:\n")

if story_id == 1:
    story1()

elif story_id == 2:
    story2()

elif story_id == 3:
    story3()

else:
    print("story selection error!")