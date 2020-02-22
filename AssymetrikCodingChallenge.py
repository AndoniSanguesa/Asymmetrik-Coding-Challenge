from BusinessCardParser import BusinessCardParser
import tkinter as tk


def updateOutput(thisContact):
    outputText.delete("1.0", "end")
    outputText.insert("1.0", "Name: " + thisContact.getName() + "\nPhone: " + thisContact.getPhoneNumber() + "\nEmail: " +
                      thisContact.getEmailAddress())


def submit():
    text = inputText.get("1.0", "end")
    if text == "\n":
        return None
    with open("input", "w") as inp:
        inp.write(text)
        inp.close()
    thisContact = BusinessCardParser("input").getContact()
    updateOutput(thisContact)


mainWin = tk.Tk()

inputLabel = tk.Label(mainWin, text="Input:")
inputLabel.grid()

inputText = tk.Text(mainWin, width=50, height=20)
inputText.grid()

outputLabel = tk.Label(mainWin, text="Output:")
outputLabel.grid()

outputText = tk.Text(mainWin, width=50, height=20)
outputText.grid()

submitButton = tk.Button(mainWin, text='Submit', width=20, command=submit)
submitButton.grid()

mainWin.mainloop()
contact = BusinessCardParser("input")

