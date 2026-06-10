import tkinter as tk
from tkinter import filedialog  

class InterfaceGrafica(tk.Tk):
    def __init__(self):
        #construtor da superclasse Tk
        super().__init__()

        # saidas relevantes para a main
        self.bpm = 100
        self.volume = 30
        self.listaDeInstrumentos = [int(-1) for i in range(16)]
        self.mandarEntrada = False
        self.tocar = False
        self.pausar = False
        self.gerarMIDI = False

        #
        # widgets e configuracoes da tkinter
        #
        self.title("Explorador de Arquivos")
        self.geometry("800x600")
        self.configure(bg="white")
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(1, weight=10)
        self.vcmd = self.register(self.input_e_numero)

        self.volumeFrame = tk.Frame(self)
        self.volumeFrame.grid(row=1,column=1,sticky ="sw")
        self.instrumentosFrame = tk.Frame(self)
        self.instrumentosFrame.grid(row = 8,column = 1,sticky = "w")
        self.controlesFrame = tk.Frame(self)
        self.controlesFrame.grid(row=9,column=1)

        self.label_file_explorer = tk.Label(self, text="No file selected", bg="white")
        self.label_file_explorer.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.button_arq = tk.Button(
            self.volumeFrame,
            text="Importar Arquivo",
            bg="lightgray",
            activebackground="gray",
            cursor="hand2",
            command=self.browseFiles
        )
        self.button_arq.grid(row=0, column=0, sticky='se')

        self.inputtxt = tk.Text(self, height = 10, width = 25, bg = "light yellow")
        self.inputtxt.grid(row=1, column=0, rowspan=10, sticky='nsew', padx=10, pady=10)

        slider_label = tk.Label(
            self.volumeFrame, 
            text='Volume:'
        )
        slider_label.grid(
            column=0,
            row=1,
            sticky='w'
        )

        slider = tk.Scale(
            self.volumeFrame,
            from_=0,
            to=127,
            orient='horizontal', 
            variable=self.volume
        )
        slider.grid(
            column=0,
            columnspan =2,
            row=2,
            sticky='we'
        )

        self.bpmLabel = tk.Label(self,text = "bpm inicial : 100")
        self.bpmLabel.grid(row=4,column=1,sticky="w")

        self.barrinhaBpm = tk.Entry(self,validate = "key", validatecommand=(self.vcmd, '%P'),width = 10)
        self.barrinhaBpm.grid(row=5,column=1,sticky = "ew")

        self.botaoBpm = tk.Button(self,text = "confirmar Bpm",command = self.muda_bpm_inicial)
        self.botaoBpm.grid(row=6,column=1,sticky = "w")

        self.instruIndice = 0

        self.instrumentosLbl = tk.Label(self,text = "Selecione intrumentos iniciais [linha][instrumento MIDI]")
        self.instrumentosLbl.grid(row = 7,column =1,sticky = "w")

        self.instruSetaEsq = tk.Button(self.instrumentosFrame,text = "<",command = self.diminui_instuIndice)
        self.instruSetaEsq.pack(side = "left")

        self.instruIndiceIn = tk.Entry(self.instrumentosFrame,width =3,validate = "key", validatecommand=(self.vcmd, '%P'))
        self.instruIndiceIn.pack(side = "left")
        self.instruIndiceIn.insert(0,1)

        self.instruSetaDir = tk.Button(self.instrumentosFrame,text = ">",command = self.aumenta_instruIndice)
        self.instruSetaDir.pack(side = "left")

        self.instruTipo = tk.Entry(self.instrumentosFrame,width =3,validate = "key", validatecommand=(self.vcmd, '%P'))
        self.instruTipo.pack(side = "left")
        self.instruTipo.insert(0,'')

        self.instrumentoConfirma = tk.Button(self.instrumentosFrame,text = "confirma",command = self.confirmar_instrumento)
        self.instrumentoConfirma.pack(side ="left")

        self.confirmarEntradas = tk.Button(self.controlesFrame,text ="ler Entrada",command = self.chama_confirmar_entradas)
        self.confirmarEntradas.pack(side = "left")

        self.botaoTocar = tk.Button(self.controlesFrame,text = "Tocar",command = self.chama_tocar)
        self.botaoTocar.pack(side = "left")

        self.botaoPausar = tk.Button(self.controlesFrame,text = "Pausar",command = self.chama_pausar)
        self.botaoPausar.pack(side="left")

        self.botaoGerarMIDI = tk.Button(self.controlesFrame,text = "Gerar MIDI",command = self.chama_gerarMIDI)
        self.botaoGerarMIDI.pack(side = "left")

        self.mensagemControles = tk.Label(self,text = "Em aguardo")
        self.mensagemControles.grid(row=10,column =1)

    
    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.txt*"),
                                                        ("all files",
                                                            "*.*")))
        self.label_file_explorer.configure(text="File Opened: "+filename)
        with open(filename, 'r') as file:
            content = file.read()
            self.inputtxt.delete(1.0, tk.END)
            self.inputtxt.insert(tk.END, content)
    
    def input_e_numero(self,textoMandado):
        if textoMandado == "":
            return True
        elif textoMandado.isdigit():
            return True
        return False
    
    def muda_bpm_inicial(self):
        bpmtemp = int(self.barrinhaBpm.get())
        if bpmtemp > 0 and bpmtemp < 401:
            self.bpm = bpmtemp
            self.bpmLabel.config(text = str(f"bpm inicial :{str(self.bpm)}"))
        else:
            self.bpmLabel.config(text = str(f"bpm inicial : erro, deve estar entre 0 e 400"))
    
    def diminui_instuIndice(self):
        if self.instruIndice > 0:
            self.instruIndice -= 1
            self.instruIndiceIn.delete(0,"end")
            self.instruIndiceIn.insert(0,str(self.instruIndice+1))
            self.instruTipo.delete(0,"end")
            self.instruTipo.insert(0,str(self.listaDeInstrumentos[self.instruIndice]))
        else:
            pass

    def aumenta_instruIndice(self):
        if  self.instruIndice < 15:
            self.instruIndice += 1
            self.instruIndiceIn.delete(0,"end")
            self.instruIndiceIn.insert(0,str(self.instruIndice+1))
            self.instruTipo.delete(0,"end")
            self.instruTipo.insert(0,str(self.listaDeInstrumentos[self.instruIndice]))
        else:
            pass

    def confirmar_instrumento(self):
        self.listaDeInstrumentos[self.instruIndice] = int(self.instruTipo.get())

    def chama_confirmar_entradas(self):
        self.mandarEntrada = True
        self.mensagemControles.config(text = "Entrada de texto Recebida")

    def chama_tocar(self):
        self.tocar = True
        self.mensagemControles.config(text = "Gerando e tocando música")

    def chama_pausar(self):
        self.pausar = True
        self.mensagemControles.config(text = "Pausado")
        
    def chama_gerarMIDI(self):
        self.gerarMIDI = True
        self.mensagemControles.config(text = "Gerando MIDI")
