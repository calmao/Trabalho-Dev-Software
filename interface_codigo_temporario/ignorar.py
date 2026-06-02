
import tkinter as tk

def butonado():
    master.destroy()

def show_input():
    lbl.config(text=f"Input: {txt.get('1.0', 'end-1c')}")


master = tk.Tk()
master.geometry("1100x700")
#master.configure(bg ="black")

botaoFechar = tk.Button(master, 
                   text="fechar", 
                   command=butonado,
                   anchor="center",
                   font=("Arial", 16),
                   height=1,
                   highlightbackground="black",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   width=15,
                   wraplength=100)
botaoFechar.pack()

btn = tk.Button(master, text="Print", command=show_input)
btn.pack()

txt = tk.Text(master, height=5, width=40)
txt.pack()

lbl = tk.Label(master, text="")
lbl.pack()

master.mainloop()

