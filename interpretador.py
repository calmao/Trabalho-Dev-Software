import mido

class Nota:
    def __init__(self, freq:str, bpm, vol:int, inst:int):
        self.freq = freq
        self.bpm = bpm
        self.vol = vol
        self.inst = inst
    
    def __str__(self):
        return f"{self.freq}"
    
class Interpretador:
    def __init__(self):
        self.partitura = []
    

    def transcrever(self, texto:str, bpm, instrumentos, volumes): # (str, list[float], list[int], list[int], list[int])
        
        if (bpm == -1):
            bpm = 100

        linhas = texto.splitlines()
        oitava,instrumentos,volumes = self.iniciar_parametros(linhas,instrumentos,volumes)

        
        for indice_voz, linha in enumerate(linhas):
            ultimo_char_nota = False #verdadeiro se, e somente se, o ultimo caracter lido for uma nota
            oitava_ini = oitava[indice_voz]

            voz = []

            delay_voz = 0
            if linha[0] == "[":
                delay_voz = int(linha[1:linha.rfind("]")])
                for indice_voz in range(delay_voz):
                    voz.append(Nota("-", bpm, volumes[indice_voz], instrumentos[indice_voz]))
            
            for indice_char in range(delay_voz, len(linha)):
                match linha[indice_char]: #primeiro switch/case case trata de ações, se cair no default entra no switch/case de notas
                    
                    case "!":
                        instrumentos[indice_voz] = 24
                        ultimo_char_nota = False
                    case "I" | "i" | "O" | "o" | "U" | "u":
                        instrumentos[indice_voz] = 110
                        ultimo_char_nota = False
                    case ";" | "1" | "3" | "5" | "7" | "9":
                        instrumentos[indice_voz] = 15
                        ultimo_char_nota = False
                    case "0":
                        ultimo_char_nota = False
                    case "2":
                        instrumentos[indice_voz] = instrumentos[indice_voz] + 2
                        ultimo_char_nota = False
                    case "4":
                        instrumentos[indice_voz] = instrumentos[indice_voz] + 4
                        ultimo_char_nota = False
                    case "6":
                        instrumentos[indice_voz] = instrumentos[indice_voz] + 6
                        ultimo_char_nota = False
                    case "8":
                        instrumentos[indice_voz] = instrumentos[indice_voz] + 8
                        ultimo_char_nota = False
                    case "?":
                        oitava[indice_voz] += 1
                        if oitava[indice_voz] ==10:
                            oitava[indice_voz]= oitava_ini
                        ultimo_char_nota = False
                    case "V":
                        oitava[indice_voz] -= 1
                        if oitava[indice_voz] == -2:
                            oitava[indice_voz]= oitava_ini
                        ultimo_char_nota = False
                    case ">":
                        bpm += 10
                        ultimo_char_nota = False
                    case "<":
                        bpm -= 10
                        ultimo_char_nota = False
                    case " ":
                        volumes[indice_voz] = 2*volumes[indice_voz]
                        if volumes[indice_voz] > 127:
                            volumes[indice_voz] = 127
                        ultimo_char_nota = False
                    case 'C':
                        voz.append(Nota((oitava[indice_voz]+1)*12, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case 'D':
                        voz.append(Nota(((oitava[indice_voz]+1)*12)+2, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case 'M':
                        voz.append(Nota(((oitava[indice_voz]+1)*12)+3, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case 'E':
                        voz.append(Nota(((oitava[indice_voz]+1)*12)+4, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case 'F':
                        voz.append(Nota(((oitava[indice_voz]+1)*12)+5, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case 'G':
                        voz.append(Nota(((oitava[indice_voz]+1)*12)+7, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case 'A':
                        voz.append(Nota(((oitava[indice_voz]+1)*12)+9, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case 'H':
                        voz.append(Nota(((oitava[indice_voz]+1)*12)+10, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case 'B':
                        voz.append(Nota(((oitava[indice_voz]+1)*12)+11, bpm, volumes[indice_voz], instrumentos[indice_voz]))
                        ultimo_char_nota = True
                    case _:
                        if (ord(linha[indice_char]) > 96 and ord(linha[indice_char]) < 105):
                            if(linha[indice_char] != "b" or linha[indice_char-1] != "M"):
                                voz.append(Nota("-", bpm, volumes[indice_voz], instrumentos[indice_voz]))
                                ultimo_char_nota = False
                        elif ultimo_char_nota:
                            voz.append(voz[-1])
                            ultimo_char_nota = False
                        
            self.partitura.append(voz)
    
    def iniciar_parametros(self,linhas,instrumentos,volumes):
        oitava = []
        for indice_voz in range(len(linhas)):
            match(indice_voz%4):
                case 0:
                    if( self.valor_invalido(instrumentos[indice_voz]) ):
                        instrumentos[indice_voz] = 0
                    if( self.valor_invalido (volumes[indice_voz]) ):
                        volumes[indice_voz] = 100
                    oitava.append(6)
                case 1:
                    if( self.valor_invalido(instrumentos[indice_voz]) ):
                        instrumentos[indice_voz] = 20
                    if( self.valor_invalido (volumes[indice_voz]) ):
                        volumes[indice_voz] = 80
                    oitava.append(5)

                case 2:
                    if( self.valor_invalido(instrumentos[indice_voz]) ):
                        instrumentos[indice_voz] = 6
                    if( self.valor_invalido(volumes[indice_voz]) ):
                        volumes[indice_voz] = 60
                    oitava.append(4)

                case 3:
                    if( self.valor_invalido(instrumentos[indice_voz]) ):
                        instrumentos[indice_voz] = 71
                    if( self.valor_invalido (volumes[indice_voz]) ):
                        volumes[indice_voz] = 40
                    oitava.append(3)

        return oitava,instrumentos,volumes

    def valor_invalido(self,valor):

        if not(valor >=0 or valor <= 127):
            invalido = True
        else:
            invalido = False

        return invalido

