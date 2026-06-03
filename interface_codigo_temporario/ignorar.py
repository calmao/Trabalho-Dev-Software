
import tkinter as tk

def carregar_txt():
    nomeDoArquivo = str(f"input_files/{ inTxtNome.get()}")
    if(nomeDoArquivo):
        arquivo = open(nomeDoArquivo)
        textoDoArquivo = arquivo.read()
        arquivo.close()

        textoInput.delete(1.0,tk.END)
        textoInput.insert(1.0,textoDoArquivo)
    

tela_interface = tk.Tk()
tela_interface.title("INTERFACE")
tela_interface.geometry("900x550")
tela_interface.configure(bg="white")
tela_interface.columnconfigure(0,weight=1)
tela_interface.rowconfigure(0,weight=1)
tela_interface.columnconfigure(1,weight=2)

textoInput = tk.Text(tela_interface)
textoInput.grid(row=0,column=0,sticky="nsew")

frame = tk.Frame(tela_interface,bg = "lightblue")
frame.grid(row = 0,column = 1,sticky="nsew")
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=0)
frame.rowconfigure(1,weight=0)
frame.rowconfigure(2,weight=1)

inTxtLbl = tk.Label(frame,text = "insira o nome do arquivo <nome.txt>")
inTxtLbl.grid(row=0,column=0,sticky="w")

inTxtNome = tk.Entry(frame)
inTxtNome.grid(row=1,column=0,sticky="ew")

inTxtConfirm = tk.Button(frame,text="carregar",command=carregar_txt)
inTxtConfirm.grid(row=2,column=0,sticky="nw")

tela_interface.mainloop()
