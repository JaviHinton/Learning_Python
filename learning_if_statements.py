# This program was my first introduction to if statements, where I learnt about conditionals


character_name = "Javi"
character_age = "25"
is_male = True

print("\nThere once was a man called " + character_name)
print("He told me he was " + character_age + " years old!")

if is_male == True:
    print(character_name + " is a man")
elif is_male == False:
    print(character_name + " is a woman")
else:
    print("we do not know the gender of " + character_name.upper())

name_length = len(character_name)
name_fletter = character_name[0]
print("")
print("The character's name has " + str(name_length) + " characters")
print("The first character in their name is: " + name_fletter)



