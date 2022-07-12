## Cryptography Encryption System 

from tkinter import *

root = Tk()
title = root.title("What's Your Secret?")
size = root.geometry("600x320")
label=Label(root, text="What's Your Secret?", font=("Lucida 22"))
label.grid(row = 0, column = 2)

label1 = Label(root, text = "Type In Your Secret Here:")               
label1.grid(row = 40, column = 1)
label2 = Label(root, text = "Your Hidden Secret is:")
label2.grid(row = 80, column = 1)
spacer1 = Label(root, text="")
spacer1.grid(row=92, column=0)
spacer2 = Label(root, text="")
spacer2.grid(row=1, column=0)
label3 = Label(root, text = "Your Hidden Message is:")               
label3.grid(row = 100, column = 1)
label4 = Label(root, text = "Your Revealed Message is:")
label4.grid(row = 200, column = 1)

entry1 = Entry(root, show = "*")
entry1.grid(row = 40, column = 2)
entry2 = Entry(root)
entry2.grid(row = 80, column = 2)
entry3 = Entry(root)
entry3.grid(row = 100, column = 2)
entry4 = Entry(root)
entry4.grid(row = 200, column = 2)

keys = "abcdefghijklmnopqrstuvwxyz !"
values = keys[-1] + keys[0:-1] 
encryptDict = dict(zip(keys, values))
decryptDict = dict(zip(values, keys))


def encryptt():
    secret = entry1.get()
    newmessage1 = "".join([encryptDict[letter] for letter in secret.lower()])
    entry2.insert(0, newmessage1)
    return newmessage1
    return entry2 

def decryptt():
    message = entry3.get()
    newmessage2 = "".join([decryptDict[letter] for letter in message.lower()])
    entry4.insert(0, newmessage2)

def saveencryption():
    f = open("Secrets.txt", "a")
    f.write(entry2.get() + "\n")
    f.close()

def opensecrets():
    newWindow = Toplevel()
    newWindow.title("Your Saved Secrets!")
    newWindow.geometry("600x320")
    newlabel=Label(newWindow, text="Your Saved Secrets!", font=("Lucida 22"))
   
    newlabel.grid(row = 0, column = 2)
    f = open("Secrets.txt", "r")
    text1=Label(newWindow, text=f.read())
    text1.grid(row = 2, column = 2)
 

encbutton = Button(root, text = "Hide Your Secret!", fg = "purple", command = encryptt)
encbutton.grid(row = 90, column = 2)
decbutton = Button(root, text = "Reveal Your Secret!", fg = "purple", command = decryptt)
decbutton.grid(row = 250, column = 2)
savebutton = Button(root, text = "Save This Secret!!", fg = "magenta", command = saveencryption)
savebutton.grid(row = 91, column = 2)
seesaved = Button(root, text = "See Encrypted Secrets!", fg = "magenta", command = opensecrets)
seesaved.grid(row = 310, column = 2)

exitbutton = Button(root, text="Exit", fg = "purple", command=root.destroy)
exitbutton.grid(row = 0, column = 0)

root.mainloop()

