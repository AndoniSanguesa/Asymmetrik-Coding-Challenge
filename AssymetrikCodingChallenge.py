from BusinessCardParser import BusinessCardParser
import tkinter as tk


# Updates the output text box with the information of the contact
def updateOutput(thisContact):
    outputText.delete("1.0", "end")
    outputText.insert("1.0", "Name: " + thisContact.getName() + "\nPhone: " + thisContact.getPhoneNumber() + "\nEmail: " +
                      thisContact.getEmailAddress())


# Handles button press by taking input text and passing it to the BuisnessCardParser
def submit():
    text = inputText.get("1.0", "end")
    if text == "\n":
        return None
    with open("input", "w") as inp:
        inp.write(text)
        inp.close()
    thisContact = BusinessCardParser("input").getContact()
    updateOutput(thisContact)


# Creates the tkinter main window
mainWin = tk.Tk()

# Input label above input text box
inputLabel = tk.Label(mainWin, text="Input:")
inputLabel.grid()

# Creates input text box
inputText = tk.Text(mainWin, width=50, height=20)
inputText.grid()

# Output label above output text box
outputLabel = tk.Label(mainWin, text="Output:")
outputLabel.grid()

# Creates output text box
outputText = tk.Text(mainWin, width=50, height=20)
outputText.grid()

# Creates the submit button that produces an output
submitButton = tk.Button(mainWin, text='Submit', width=20, command=submit)
submitButton.grid()

# Loop for tkinter
mainWin.mainloop()

