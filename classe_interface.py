import tkinter as tk
from tkinter import filedialog
import musica  
import inputLista as il
import interpretador
import tocarComPygame as tCP

class InterfaceGrafica(tk.Tk):
    def __init__(self):

        super().__init__()

        # saidas relevantes para o programa
        self.saidaMIDI = musica.Musica()
        self.bpm = 100
        self.listaDeVolumes = [100 for i in range (16)]
        self.listaDeInstrumentos = [int(-1) for i in range(16)]
        self.textoParaConverter =  " "
        self.entradaRecebida = False
        self.musicaPausada = False

        #
        # widgets e configuracoes da tkinter
        #
        self.title("GERADOR DE SEQUENCIAS MUSICAIS    DesSoft-2026/1")
        self.geometry("800x600")
        self.configure(bg="white")
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(1, weight=10)
        self.vcmd = self.register(self.input_e_numero)

        self.controlesFrame = tk.Frame(self)
        self.controlesFrame.grid(row=10,column=1)


        #importador de arquivo
        self.label_file_explorer = tk.Label(self, text="Nenhum arquivo selecionado", bg="white")
        self.label_file_explorer.grid(row=0, column=0,columnspan=2, padx=10, pady=5, sticky="w")

        self.button_arq = tk.Button(
            self,
            text="Importar Arquivo",
            bg="lightgray",
            activebackground="gray",
            cursor="hand2",
            command=self.browseFiles
        )
        self.button_arq.grid(row=1, column=1, sticky='sw',pady = 20)

        #selecao de BPM inicial
        self.inputtxt = tk.Text(self, height = 10, width = 25, bg = "light yellow")
        self.inputtxt.grid(row=1, column=0, rowspan=10, sticky='nsew', padx=10, pady=10)

        self.bpmLabel = tk.Label(self,text = "BPM inicial : 100")
        self.bpmLabel.grid(row=4,column=1,sticky="w")

        self.barrinhaBpm = tk.Entry(self,validate = "key", validatecommand=(self.vcmd, '%P'),width = 10)
        self.barrinhaBpm.grid(row=5,column=1,sticky = "w")

        self.botaoBpm = tk.Button(self,text = "Confirmar BPM",command = self.muda_bpm_inicial)
        self.botaoBpm.grid(row=6,column=1,sticky = "w")

        #comandos finais do usuario
        self.confirmarEntradas = tk.Button(self.controlesFrame,text ="Ler Entrada",command = self.chama_confirmar_entradas)
        self.confirmarEntradas.pack(side = "left")

        self.botaoTocar = tk.Button(self.controlesFrame,text = "Tocar",command = self.chama_tocar)
        self.botaoTocar.pack(side = "left")

        self.botaoPausar = tk.Button(self.controlesFrame,text = "Pausar",command = self.chama_pausar)
        self.botaoPausar.pack(side="left")

        self.botaoGerarMIDI = tk.Button(self.controlesFrame,text = "Gerar MIDI",command = self.chama_gerarMIDI)
        self.botaoGerarMIDI.pack(side = "left")

        self.mensagemControles = tk.Label(self,text = "Em aguardo")
        self.mensagemControles.grid(row=11,column =1)

        #widgets para gerar lista de volumes e lista de instrumentos
        self.instrumentos = il.InputDeListaDeParametros(self,"instrumentos",self.vcmd,0)
        self.instrumentos.grid(row = 7,column = 1,sticky = "w",pady = 10)

        self.volumes = il.InputDeListaDeParametros(self,"volumes",self.vcmd,100)
        self.volumes.grid(row = 8,column =1,sticky = "w",pady = 10)

    
    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = [('Allowed Types', '*.txt')])
        self.label_file_explorer.configure(text="Arquivo aberto: "+filename)
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
        if bpmtemp >= 1 and bpmtemp <= 400:
            self.bpm = bpmtemp
            self.bpmLabel.config(text = str(f"BPM inicial :{str(self.bpm)}"))
        else:
            self.bpmLabel.config(text = str(f"BPM inicial : Erro, deve estar entre 1 e 400"))

    def chama_confirmar_entradas(self):
        self.textoParaConverter = self.inputtxt.get(1.0,"end-1c")


        self.listaDeInstrumentos = self.instrumentos.listaDeSaida
        self.listaDeVolumes = self.volumes.listaDeSaida
        
        self.entradaRecebida = True
        self.mensagemControles.config(text = "Entrada de texto Recebida")

        interpretado = interpretador.Interpretador()
        interpretado.transcrever(self.textoParaConverter,
                                 self.bpm,self.listaDeInstrumentos,self.listaDeVolumes)
        self.saidaMIDI.iniciar(interpretado)

    def chama_tocar(self):
        if(self.entradaRecebida):
            self.saidaMIDI.salvar("MIDI.mid")
            tCP.tocar_arquivoMIDI("Saidas/MIDI.mid")
            self.musicaPausada = False
            self.botaoPausar.config(text="Pausar")
            self.mensagemControles.config(text = "Gerando e tocando música")
        else:
            self.mensagemControles.config(text = "Erro: nenhuma entrada confirmada")

    def chama_pausar(self):
        if not self.entradaRecebida:
            self.mensagemControles.config(text = "Erro: nenhuma entrada confirmada")
            return

        if self.musicaPausada:
            tCP.despausar_arquivoMIDI()
            self.musicaPausada = False
            self.botaoPausar.config(text="Pausar")
            self.mensagemControles.config(text = "Continuando música")
        else:
            tCP.pausar_arquivoMIDI()
            self.musicaPausada = True
            self.botaoPausar.config(text="Continuar")
            self.mensagemControles.config(text = "Música pausada")
        
    def chama_gerarMIDI(self):
        if(self.entradaRecebida):
            self.saidaMIDI.salvar("MIDI.mid")
            self.mensagemControles.config(text = "Gerando MIDI")
        else:
            self.mensagemControles.config(text = "Erro: nenhuma entrada confirmada")


def main():
    interface = InterfaceGrafica()
    interface.mainloop()

if __name__ == "__main__":
    main()