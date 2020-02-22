import re
from ContactInfo import ContactInfo


class BusinessCardParser:
    def __init__(self, inputDocument):
        self.phone_number_re = [re.compile(r'd{3}\W\d{3}\W\d{4}'), re.compile(r'\W\d{3}\W\s\d{3}\s\d{4}'),
                           re.compile(r'\W\d{3}\W{2}\d{3}\W\d{4}'), re.compile(r'\d{3}\s\d{3}\s\d{4}'),
                           re.compile(r'\W\d{3}\W\s\d{3}\s\d{4}'), re.compile(r'\d{10}'), re.compile(r'\d{3}\s\d{7}'),
                           re.compile(r'\W\d{3}\W\d{3}\W\d{4}'), re.compile(r'\W\d{3}\W\d{3}\s\d{4}')]
        self.name = ""
        self.email = ""
        self.phone = ""
        self.names = set([])
        self.contact = None

        # Adds all names from the SortedNames dataset to a set
        with open("SortedNames") as sn:
            aName = sn.readline()
            while aName:
                self.names.add(aName.replace("\n", ""))
                aName = sn.readline()

        # Checks each line to see if it contains a name, phone number or email
        with open(inputDocument) as inp:
            lines = inp.readlines()
            for line in lines:
                self.name = self.containsName(line) if self.name == "" else self.name
                self.phone = self.containsPhoneNumber(line) if self.phone == "" else self.phone
                self.email = self.containsEmail(line) if self.email == "" else self.email
            self.contact = ContactInfo(self.name, self.phone, self.email)
            inp.close()

    # Checks if there is a name in the line by checking if the first name is in the names set
    def containsName(self, inline):
        first_name = inline.split()[0]
        if first_name.lower() in self.names:
            return inline.replace("\n", "")
        return self.name

    # Checks if there is an email in the line by checking for the '@' Character
    def containsEmail(self, inline):
        if "@" in inline:
            return inline
        return self.email

    # Checks for a phone number by first trying to pattern match with a number of regex in an array above, then all
    # non-numeric characters are deleted
    def containsPhoneNumber(self, inline):
        inline = inline.lower()
        if "fax" in inline:
            return self.phone
        for reg in self.phone_number_re:
            match = reg.search(inline)
            if match is not None:
                match = match.string
                match = re.sub("[^0-9]", "", match)
                return match
        return self.phone

    # Returns the contact defined by the information that was passed in
    def getContact(self):
        return self.contact
