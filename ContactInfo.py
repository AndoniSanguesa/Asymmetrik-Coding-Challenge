class ContactInfo:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phone

    def getEmailAddress(self):
        return self.email

    def printInfo(self):
        print("Name: " + self.getName())
        print("Phone: " + self.getPhoneNumber())
        print("Email: " + self.getEmailAddress())
