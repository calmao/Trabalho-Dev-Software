
import tkinter as tk

def butonado():
    master.destroy()

def show_input():
    lbl.config(text=f"Input: {txt.get('1.0', 'end-1c')}")


master = tk.Tk()
master.geometry("1100x700")
master.title("INTERFACE EXPERIMENTAL")
master.configure(bg ="white")

botaoFechar = tk.Button(master, 
                   text="Fechar", 
                   command=butonado,
                   anchor="center",
                   font=("Arial", 16),
                   highlightbackground="lightblue",
                   highlightthickness=2,
                   justify="center",
                   height=1,
                   width=7,)
botaoFechar.grid(row =0,column =0,sticky = "w")

btn = tk.Button(master, text="Print", command=show_input,
                anchor="center",
                font=("Arial", 16),
                highlightbackground="lightblue",
                highlightthickness=2,
                justify="center",
                height=1,
                width=7,)
btn.grid(row =1,column =0,sticky = "w")

txt = tk.Text(master, height=20, width=70,highlightbackground="lightblue")
txt.grid(row =3,column = 0)

lbl = tk.Label(master, text="aperte print para replicar a entrada :)")
lbl.grid(row =4,column =0,sticky = "w")

master.mainloop()

