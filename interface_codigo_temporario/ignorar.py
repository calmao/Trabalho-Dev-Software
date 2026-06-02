
import tkinter as tk

def butonado():
    print("printar")


master = tk.Tk()
master.geometry("1100x700")
master.configure(bg ="lightblue")

botaoFechar = tk.Button(master, 
                   text="FECHAR", 
                   command=butonado,
                   anchor="center",
                   font=("Arial", 16),
                   height=2,
                   highlightbackground="black",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
botaoFechar.pack()

master.mainloop()

