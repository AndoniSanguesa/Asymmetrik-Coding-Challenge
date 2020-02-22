import re

phone_number_re = [re.compile(r'd{3}\W\d{3}\W\d{4}'), re.compile(r'\W\d{3}\W\s\d{3}\s\d{4}'),
                   re.compile(r'\W\d{3}\W{2}\d{3}\W\d{4}'), re.compile(r'\d{3}\s\d{3}\s\d{4}'),
                   re.compile(r'\W\d{3}\W\s\d{3}\s\d{4}'), re.compile(r'\d{10}'), re.compile(r'\d{3}\s\d{7}'),
                   re.compile(r'\W\d{3}\W\d{3}\W\d{4}'), re.compile(r'\W\d{3}\W\d{3}\s\d{4}')]
name = ""
phone = ""
email = ""
names = set([])

with open("SortedNames") as sn:
    aName = sn.readline()
    while aName:
        names.add(aName.replace("\n", ""))
        aName = sn.readline()


def contains_name(inline):
    first_name = inline.split()[0]
    if first_name.lower() in names:
        return inline.replace("\n", "")
    return name


def contains_email(inline):
    if "@" in inline:
        return inline
    return phone


def contains_phone_number(inline):
    inline = inline.lower()
    if "fax" in inline:
        return phone
    for reg in phone_number_re:
        match = reg.search(inline)
        if match is not None:
            match = match.string
            match = re.sub("[^0-9]", "", match)
            return match
    return phone


with open("input") as inp:
    lines = inp.readlines()

    for line in lines:
        name = contains_name(line)
        phone = contains_phone_number(line)
        email = contains_email(line)
    print(name)
    print(phone)
    print(email)
    inp.close()
