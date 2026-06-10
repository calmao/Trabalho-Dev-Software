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



root.configure(bg="white")

# layout: duas colunas (0 = área principal, 1 = controles)
root.columnconfigure(0, weight=10)
root.columnconfigure(1, weight=0)
root.rowconfigure(1, weight=10)

label_file_explorer = tk.Label(root, text="No file selected", bg="white")
label_file_explorer.grid(row=0, column=0, padx=10, pady=5, sticky="w")

volumeFrame = tk.Frame(root)
volumeFrame.grid(row=1,column=1,sticky ="sw")

button_arq = tk.Button(
    volumeFrame,
    text="Importar Arquivo",
    bg="lightgray",
    activebackground="gray",
    cursor="hand2",
    command=browseFiles
)
# colocar controles na coluna da direita
button_arq.grid(row=0, column=0, sticky='se')

# slider current value
current_value = tk.DoubleVar()

slider_label = tk.Label(
    volumeFrame, 
    text='Volume:'
)

slider_label.grid(
    column=0,
    row=1,
    sticky='w'
)

#  slider
slider = tk.Scale(
    volumeFrame,
    from_=0,
    to=127,
    orient='horizontal',  # vertical
    variable=current_value
)

slider.grid(
    column=0,
    columnspan =2,
    row=2,
    sticky='we'
)

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
    if bpmtemp > 0 and bpmtemp < 401:
        bpmInicial = bpmtemp
        bpmLabel.config(text = str(f"bpm inicial :{str(bpmInicial)}"))
    else:
        bpmLabel.config(text = str(f"bpm inicial : erro, deve estar entre 0 e 400"))


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
    if instruIndice > 0:
        instruIndice -= 1
        instruIndiceIn.delete(0,"end")
        instruIndiceIn.insert(0,str(instruIndice+1))
        instruTipo.delete(0,"end")
        instruTipo.insert(0,str(listaInstrumentos[instruIndice]))
    else:
        pass

def aumenta_instruIndice():
    global instruIndice
    global listaInstrumentos
    if  instruIndice < 15:
        instruIndice += 1
        instruIndiceIn.delete(0,"end")
        instruIndiceIn.insert(0,str(instruIndice+1))
        instruTipo.delete(0,"end")
        instruTipo.insert(0,str(listaInstrumentos[instruIndice]))
    else:
        pass

def confirmar_instrumento():
    global instruIndice
    global listaInstrumentos
    listaInstrumentos[instruIndice] = int(instruTipo.get())


listaInstrumentos = [int(-1) for i in range(16)]
instruIndice = 0

instrumentosLbl = tk.Label(root,text = "Selecione intrumentos iniciais [linha][instrumento MIDI]")
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

#botoes do usuario
# mandar entrada, tocar, pausar, gerar arquivo
mandarEntrada = False
tocar = False
pausar = False
gerarMIDI = False

def chama_confirmar_entradas():
    global mandarEntrada
    global mensagemControles
    mandarEntrada = True
    mensagemControles.config(text = "Entrada de texto Recebida")


def chama_tocar():
    global tocar
    global mensagemControles
    tocar = True
    mensagemControles.config(text = "Gerando e tocando música")

def chama_pausar():
    global pausar
    global mensagemControles
    pausar = True
    mensagemControles.config(text = "Pausado")
    
def chama_gerarMIDI():
    global gerarMIDI
    global mensagemControles
    gerarMIDI = True
    mensagemControles.config(text = "Gerando MIDI")

controlesFrame = tk.Frame(root)
controlesFrame.grid(row=9,column=1)

confirmarEntradas = tk.Button(controlesFrame,text ="ler Entrada",command = chama_confirmar_entradas)
confirmarEntradas.pack(side = "left")

botaoTocar = tk.Button(controlesFrame,text = "Tocar",command = chama_tocar)
botaoTocar.pack(side = "left")

botaoPausar = tk.Button(controlesFrame,text = "Pausar",command = chama_pausar)
botaoPausar.pack(side="left")

botaoGerarMIDI = tk.Button(controlesFrame,text = "Gerar MIDI",command = chama_gerarMIDI)
botaoGerarMIDI.pack(side = "left")

mensagemControles = tk.Label(root,text = "Em aguardo")
mensagemControles.grid(row=10,column =1)

root.mainloop()
