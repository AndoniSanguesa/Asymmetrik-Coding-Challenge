# List of names to sort alphabetically
namesList = []

# Opens the names txt with unordered names and puts them in list 'namesList'
with open("namestxt.txt") as nt:
    line = nt.readline()
    while line:
        namesList.append(line)
        line = nt.readline()
    nt.close()

namesList.sort()

# Opens the sortedNames txt and writes the names in alphabetical order
with open("SortedNames", "w") as sn:
    for name in namesList:
        sn.write(name.lower())
    sn.close()

print(namesList)