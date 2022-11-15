acronyms = ["LOL", "IDK", "BFF", "IMHO", "TMI"]

# Printing the list
print("The acronyms are: ", acronyms)

# Printing the acronym indexwise
print("The acronyms meanings: ")
print("1: " + acronyms[0])
print("2: " + acronyms[1])
print("3: " + acronyms[2])
print("4: " + acronyms[3])
print("5: " + acronyms[4])

# Updating the list

acronyms[0] = "laugh out loud"
acronyms[1] = "I don't know"
acronyms[2] = "best friends forever"
acronyms[3] = "in my humble opinion"
acronyms[4] = "too much information"


# Appending to the list

acronyms.append("BTW")
acronyms.append("BFN")

# Printing the list
print(acronyms)

# Removing from the list
acronyms.remove('BFN')
print(acronyms)

# Removing from the list using index
acronyms.remove(acronyms[0])
print(acronyms)

# Check if an item is in the list or not

word = input("Enter a word: ")
if word in acronyms:
    print("The word exists in the list!")
else:
    print("The word does not exist in the list!")

