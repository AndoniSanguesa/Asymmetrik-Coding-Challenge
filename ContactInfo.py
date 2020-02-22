class ContactInfo:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # Returns name of contact
    def getName(self):
        return self.name

    # Returns phone number of contact
    def getPhoneNumber(self):
        return self.phone

    # Returns email address of context
    def getEmailAddress(self):
        return self.email

    # Prints the info of the contact
    def printInfo(self):
        print("Name: " + self.getName())
        print("Phone: " + self.getPhoneNumber())
        print("Email: " + self.getEmailAddress())
