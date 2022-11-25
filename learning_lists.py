friends = ["Bex", "Kayleigh", "Brandon", "James", "Harry", "Ben", "Matt"]

print("Our original list of friends is:")
print(friends)

#   We can change and append lists when we like
friends[3] = "Charlie"

#   Only viewing the 3 results. Up to but not including the 5th [4] index
print(friends[1:4])

#   Appending to the end of the list
#friends += "Javi", < realised this can be done better with the below as it does not require the ","
friends.append("Javi")
print(friends)

lottery_numbers = [12, 38, 31, 2, 46, 72, 16, 12]

#   We can append with another list
friends.extend(lottery_numbers)
print(friends)

#   We can use .insert to place something within a specific position within the list
friends.insert(8, "Lottery Numbers:")
print(friends)

#   We can remove an item by using .remove
friends.remove("Lottery Numbers:")
print(friends)

#   We can remove the last element from the end of a list with .pop
#   Helpful for removing unnecessary logs when scripting maybe...?
friends.pop()
print(friends)

#   We can search the list with .index
print(friends.index("Javi"))

#   We can count how many times something appears in a list with .count
print(friends.count(12))

#   We can wipe the list with .clear
friends.clear()
print(friends)

#  We can sort things alphabetically or numerically with .sort
# print(friends.sort()) < does not work, needs to be done separately
friends.sort()
print(friends)

# Arrays!

#   We can create a 2D list (array) by putting lists within lists
#   These must be separated with , and will be referenced with [row][column]

first_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Below should print out 5 as starting count from 0, the first column over and down points to 5
print(first_array[1][1])

# We can loop through all values by nesting
for row in first_array:
    for col in row:
        print(col)

