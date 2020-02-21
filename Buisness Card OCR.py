name = ""
phone = ""
email = ""
names = []

with open("SortedNames") as sn:
    names = sn.readlines()

def contains_name(inline):
    for name in names:
        if name.__contains__(inline):
            return True
    return False


def contains_email(inline):
    if inline.__contains__("@"):
        return True
    return False


def contains_phone_number(line):
    line = line.lower()


with open("input") as inp:
    lines = inp.readlines()

    for line in lines:
        name = line if contains_name(line) else name
        phone = line if contains_phone_number(line) else phone
        email = line if contains_email(line) else email
    inp.close()