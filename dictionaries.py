#   Dictionaries are used to reference something with another name
#   these are laid out as dictionary = {"key": "value",}
#   Dictionaries cannot have two of the same key (reference)


nicknames = {
    "Javi": "Javier",
    "javi": "Javier",
    "Bex": "Rebecca",
    "Becca": "Rebecca",
    "Becky": "Rebecca"
}
error_variable = "no key found"

print(nicknames["Javi"]) # < will only take 1 value
print(nicknames.get("Bex", error_variable)) # < will allow second value but as default return (used as error in this example)
print(nicknames.get("Rebi", error_variable))