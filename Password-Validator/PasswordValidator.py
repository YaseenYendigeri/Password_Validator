from tkinter import *
import bcrypt

root = Tk()
root.geometry("300x300")

def validate(password):
    hashed = b'$2b$12$m5bhCerLe3oTN2sO52/53Obf77MAQppXu6DuVQ2TBnmDx.uXA.KFi'
    password = bytes(password, encoding="utf-8")
    if bcrypt.checkpw(password, hashed):
        print("Login Successful.")
    else:
        print("Invalid Password.")


password_entry = Entry(root)
password_entry.pack()

button = Button(text="validate", command=lambda:validate(password_entry.get()))
button.pack()
root.mainloop()