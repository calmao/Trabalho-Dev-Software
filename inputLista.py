import tkinter as tk

class InputDeListaDeParametros(tk.Frame):
    def __init__(self,parent,inputTypeName,vcmd,valorPadrao):
        super().__init__(parent)

        self.listaDeSaida = [valorPadrao for _ in range(16)]
        self.indice = 0
        self.vcmd = vcmd

        self.tituloLbl = tk.Label(self,text = f"Selecione os {str(inputTypeName)} iniciais de cada linha")
        self.tituloLbl.pack(side = "top")

        self.SetaEsq = tk.Button(self,text = "<",command = self.diminui_indice)
        self.SetaEsq.pack(side = "left")

        self.indiceLbl = tk.Label(self,text = "1")
        self.indiceLbl.pack(side = "left")

        self.instruSetaDir = tk.Button(self,text = ">",command = self.aumenta_indice)
        self.instruSetaDir.pack(side = "left")

        self.entradaValor = tk.Entry(self,width =3,validate = "key", validatecommand=(self.vcmd, '%P'))
        self.entradaValor.pack(side = "left")
        self.entradaValor.insert(0,valorPadrao)

        self.botaoConfirma = tk.Button(self,text = "Confirma",command = self.confirmar_valor)
        self.botaoConfirma.pack(side ="left")

    def diminui_indice(self):
        if self.indice > 0:
            self.indice -= 1
            self.atualiza_entradaValor()
        else:
            pass

    def aumenta_indice(self):
        if  self.indice < 15:
            self.indice += 1
            self.atualiza_entradaValor()
        else:
            pass

    def confirmar_valor(self):
        dado = int(self.entradaValor.get())
        if dado <= 127 and dado >= 0:
            self.listaDeSaida[self.indice] = dado
        else:
            pass
    
    def atualiza_entradaValor(self):
            self.indiceLbl.configure(text = str(self.indice+1))
            self.entradaValor.delete(0,"end")
            self.entradaValor.insert(0,str(self.listaDeSaida[self.indice]))
