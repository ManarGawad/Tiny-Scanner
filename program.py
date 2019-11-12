from functions import reform_input
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *


def start():
    name = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                           title="Choose a file.")
    file = name.split("/")[-1]
    if file:
        out = reform_input(file)
        w3 = Tk()
        border = Frame(w3, bd=1, background='white')
        border.pack()
        listbox = Listbox(border, width=50, height=30, background=border.cget("background"))
        listbox.pack(side="left")
        scrollbar = Scrollbar(border, orient="vertical")
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.config(yscrollcommand=scrollbar.set)
        Button(w3, text='Quit', command=quit).pack(side='right', pady="5", padx='50')
        Button(w3, text='New File', command=start).pack(side='left', padx=50)
        for item in out:
            if item == 'error':
                showerror("ERROR", "you enter invalid input")
                break
            else:
                listbox.insert(END, item)
        out.clear()
        w3.mainloop()
    else:
        showerror("ERROR", "you enter invalid file name")


master = Tk()
Label(master, text="Let's start scan our code").grid(row=0, padx=20, pady=20)
Label(master, text="Choose file").grid(row=1, padx=20)
but = Button(master, text='Open', command=start).grid(row=2, pady=10)

master.mainloop()
