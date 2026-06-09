import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Explorador de Arquivos")
root.geometry("800x600")

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    with open(filename, 'r') as file:
        content = file.read()
        inputtxt.delete(1.0, tk.END)
        inputtxt.insert(tk.END, content)



root.configure(bg="lightblue")

# layout: duas colunas (0 = área principal, 1 = controles)
root.columnconfigure(0, weight=10)
root.columnconfigure(1, weight=0)
root.rowconfigure(1, weight=10)

label_file_explorer = tk.Label(root, text="No file selected", bg="lightblue")
label_file_explorer.grid(row=0, column=0, padx=10, pady=5, sticky="w")

button_arq = tk.Button(
    root,
    text="Importar Arquivo",
    bg="lightgray",
    activebackground="gray",
    cursor="hand2",
    command=browseFiles
)
# colocar controles na coluna da direita
button_arq.grid(row=3, column=1, padx=20, pady=10, sticky='w')

# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())

slider_label = tk.Label(
    root, 
    text='Volume:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky='e'
)

#  slider
slider = tk.Scale(
    root,
    from_=0,
    to=127,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(
    column=1,
    row=0,
    sticky='we'
)

current_value_label = tk.Label(
    root,
    text='Current Value Volume:'
)

current_value_label.grid(
    row=1,
    column =1,
    columnspan=1,
    sticky='ws',
    ipadx=10,
    ipady=10
)

value_label = tk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=2,
    column =1,
    columnspan=2,
    sticky='nw'
)

print(get_current_value())

inputtxt = tk.Text(root, height = 10, width = 25, bg = "light yellow")
inputtxt.grid(row=1, column=0, rowspan=10, sticky='nsew', padx=10, pady=10)



#validar inputs
def validar_input_numero(textoMandado):
    if textoMandado == "":
        return True
    elif textoMandado.isdigit():
        return True
    return False
vcmd = root.register(validar_input_numero)

#
#funcionalidade de input do bpm 
# codigo funciona mas pode receber mais polimento
#
def muda_bpm_inicial():
    bpmtemp = int(barrinhaBpm.get())
    if bpmtemp%5 == 0 :
        bpmInicial = bpmtemp
        bpmLabel.config(text = str(f"bpm inicial :{str(bpmInicial)}"))
    else:
        bpmLabel.config(text = str(f"bpm inicial : erro, deve ser inteiro multiplo de 5"))


bpmLabel = tk.Label(root,text = "bpm inicial : 100")
bpmLabel.grid(row=4,column=1,sticky="w")

bpmInicial = 100
barrinhaBpm = tk.Entry(root,validate = "key", validatecommand=(vcmd, '%P'),width = 10)
barrinhaBpm.grid(row=5,column=1,sticky = "ew")

botaoBpm = tk.Button(root,text = "confirmar Bpm",command = muda_bpm_inicial)
botaoBpm.grid(row=6,column=1,sticky = "w")



#gerar lista de intrumentos iniciais
def diminui_instuIndice():
    global instruIndice
    global listaInstrumentos
    if instruIndice > 1:
        instruIndice -= 1
        instruIndiceIn.delete(0,"end")
        instruIndiceIn.insert(0,str(instruIndice))
        instruTipo.delete(0,"end")
        instruTipo.insert(0,str(listaInstrumentos[instruIndice]))
    else:
        pass

def aumenta_instruIndice():
    global instruIndice
    global listaInstrumentos
    if  instruIndice < 50:
        instruIndice += 1
        instruIndiceIn.delete(0,"end")
        instruIndiceIn.insert(0,str(instruIndice))
        instruTipo.delete(0,"end")
        instruTipo.insert(0,str(listaInstrumentos[instruIndice]))
    else:
        pass

def confirmar_instrumento():
    global instruIndice
    global listaInstrumentos
    listaInstrumentos[instruIndice] = int(instruTipo.get())


listaInstrumentos = [int(-1) for i in range(1,51)]
instruIndice = 1

instrumentosLbl = tk.Label(root,text = "selecionar intrumentos iniciais [linha][instrumento]")
instrumentosLbl.grid(row = 7,column =1,sticky = "w")

instrumentosFrame = tk.Frame(root)
instrumentosFrame.grid(row = 8,column = 1,sticky = "w")

instruSetaEsq = tk.Button(instrumentosFrame,text = "<",command = diminui_instuIndice)
instruSetaEsq.pack(side = "left")

instruIndiceIn = tk.Entry(instrumentosFrame,width =3,validate = "key", validatecommand=(vcmd, '%P'))
instruIndiceIn.pack(side = "left")
instruIndiceIn.insert(0,1)

instruSetaDir = tk.Button(instrumentosFrame,text = ">",command = aumenta_instruIndice)
instruSetaDir.pack(side = "left")

instruTipo = tk.Entry(instrumentosFrame,width =3,validate = "key", validatecommand=(vcmd, '%P'))
instruTipo.pack(side = "left")
instruTipo.insert(0,'')

instrumentoConfirma = tk.Button(instrumentosFrame,text = "confirma",command = confirmar_instrumento)
instrumentoConfirma.pack(side ="left")

root.mainloop()
