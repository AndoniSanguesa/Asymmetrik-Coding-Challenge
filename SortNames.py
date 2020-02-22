namesList = []

with open("namestxt.txt") as nt:
    line = nt.readline()
    while line:
        namesList.append(line)
        line = nt.readline()
    nt.close()

namesList.sort()

with open("SortedNames", "w") as sn:
    for name in namesList:
        sn.write(name.lower())
    sn.close()

print(namesList)