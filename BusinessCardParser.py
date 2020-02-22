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

        with open("SortedNames") as sn:
            aName = sn.readline()
            while aName:
                self.names.add(aName.replace("\n", ""))
                aName = sn.readline()

        with open(inputDocument) as inp:
            lines = inp.readlines()

            for line in lines:
                self.name = self.containsName(line)
                self.phone = self.containsPhoneNumber(line)
                self.email = self.containsEmail(line)
            self.contact = ContactInfo(self.name, self.phone, self.email)
            inp.close()

    def containsName(self, inline):
        first_name = inline.split()[0]
        if first_name.lower() in self.names:
            return inline.replace("\n", "")
        return self.name

    def containsEmail(self, inline):
        if "@" in inline:
            return inline
        return self.email

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

    def getContact(self):
        return self.contact