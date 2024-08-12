from tkinter import *

def encrypte():
    replacement_dict = {
        "0": ")", "1": "!", "2": "@", "3": "#", "4": "$", 
        "5": "%", "6": "^", "7": "&", "8": "*", "9": "(",

        "A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", 
        "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", 
        "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", 
        "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", 
        "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A",

        "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", 
        "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", 
        "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", 
        "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", 
        "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a",

        "!": "1", "@": "2", "#": "3", "$": "4", "%": "5", 
        "^": "6", "&": "7", "*": "8", "(": "9", ")": "0",
        "-": "_", "_": "-", "+": "=", "=": "+", "[": "]", 
        "]": "[", "{": "}", "}": "{", ";": ":", ":": ";", 
        "'": "\"", "\"": "'", "\\": "|", "|": "\\", 
        ",": ".", ".": ",", "<": ">", ">": "<", "/": "?", "?": "/"
    }

    user_input = entry.get()
    resault = ""

    for char in user_input:
        if char in replacement_dict:
            resault += replacement_dict[char]
        else:
            resault += char  

    result_text.config(state=NORMAL) 
    result_text.delete(1.0, END)  
    result_text.insert(END, resault)  
    result_text.config(state=DISABLED)  

window = Tk()
window.title("Crypter: Powered by Anes")
window.geometry("720x600")

label = Label(window, 
              text="Encrypt Powered by Anes", 
              font=("Helvetica", 20, "bold"), 
              fg="white", 
              bg="DarkGoldenrod1", 
              padx=10, pady=10,  
              relief=RAISED,  
              borderwidth=2)  
label.pack(pady=20)  

entry = Entry(window, width=40, bg="linen", fg="gray9")
entry.pack(pady=10)

button = Button(window, text="Encrypt", command=encrypte, fg='black', bg="DarkGoldenrod1", activebackground="Red")
button.pack(pady=10)

result_text = Text(window, height=10, width=50, wrap=WORD, state=DISABLED)
result_text.pack(pady=10)

label = Label(window, 
              text="to decrypte write the output in the entry.", 
              font=("Helvetica", 20, "bold"), 
              fg="white", 
              bg="DarkGoldenrod1", 
              padx=10, pady=10,
              relief=RAISED,
              borderwidth=2)
label.pack(pady=20) 
window.mainloop()
