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
    

    def transcrever(self, texto, bpm, inst, vol): # (str, list[float], list[int], list[int], list[int])
        
        if (bpm == -1):
            bpm = 100

        oitava = []
        linhas = texto.splitlines()
        for i in range(len(linhas)):
            match(i%4):
                case 0:
                    if(inst[i] == -1):
                        inst[i] = 0
                    if(vol[i] ==-1):
                        vol[i] = 100
                    oitava.append(6)
                case 1:
                    if(inst[i] == -1):
                        inst[i] = 20
                    if(vol[i] ==-1):
                        vol[i] = 80
                    oitava.append(5)

                case 2:
                    if(inst[i] == -1):
                        inst[i] = 6
                    if(vol[i] ==-1):
                        vol[i] = 60
                    oitava.append(4)

                case 3:
                    if(inst[i] == -1):
                        inst[i] = 71
                    if(vol[i] ==-1):
                        vol[i] = 40
                    oitava.append(3)

        
        for i, l in enumerate(linhas):
            ultimo_char_nota = False #verdadeiro se, e somente se, o ultimo caracter lido for uma nota
            oitava_ini = oitava[i]

            voz = []

            a = 0
            if l[0] == "[":
                a = int(l[1:l.rfind("]")])
                for i in range(a):
                    voz.append(Nota("-", bpm, vol[i], inst[i]))
            
            for j in range(a, len(l)):
                match l[j]: #primeiro switch/case case trata de ações, se cair no default entra no switch/case de notas
                    
                    case "!":
                        inst[i] = 24
                        ultimo_char_nota = False
                    case "I" | "i" | "O" | "o" | "U" | "u":
                        inst[i] = 110
                        ultimo_char_nota = False
                    case ";" | "1" | "3" | "5" | "7" | "9":
                        inst[i] = 15
                        ultimo_char_nota = False
                    case "0":
                        inst[i] = inst[i]
                        ultimo_char_nota = False
                    case "2":
                        inst[i] = inst[i] + 2
                        ultimo_char_nota = False
                    case "4":
                        inst[i] = inst[i] + 4
                        ultimo_char_nota = False
                    case "6":
                        inst[i] = inst[i] + 6
                        ultimo_char_nota = False
                    case "8":
                        inst[i] = inst[i] + 8
                        ultimo_char_nota = False
                    case "?":
                        oitava[i] += 1
                        if oitava[i] ==10:
                            oitava[i]= oitava_ini
                        ultimo_char_nota = False
                    case "V":
                        oitava[i] -= 1
                        if oitava[i] == -2:
                            oitava[i]= oitava_ini
                        ultimo_char_nota = False
                    case ">":
                        bpm += 10
                        ultimo_char_nota = False
                    case "<":
                        bpm -= 10
                        ultimo_char_nota = False
                    case " ":
                        vol[i] = 2*vol[i]
                        if vol[i] > 127:
                            vol[i] = 127
                        ultimo_char_nota = False
                    case 'C':
                        voz.append(Nota((oitava[i]+1)*12, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case 'D':
                        voz.append(Nota(((oitava[i]+1)*12)+2, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case 'M':
                        voz.append(Nota(((oitava[i]+1)*12)+3, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case 'E':
                        voz.append(Nota(((oitava[i]+1)*12)+4, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case 'F':
                        voz.append(Nota(((oitava[i]+1)*12)+5, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case 'G':
                        voz.append(Nota(((oitava[i]+1)*12)+7, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case 'A':
                        voz.append(Nota(((oitava[i]+1)*12)+9, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case 'H':
                        voz.append(Nota(((oitava[i]+1)*12)+10, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case 'B':
                        voz.append(Nota(((oitava[i]+1)*12)+11, bpm, vol[i], inst[i]))
                        ultimo_char_nota = True
                    case _:
                        if (ord(l[j]) > 96 and ord(l[j]) < 105):
                            if(l[j] != "b" or l[j-1] != "M"):
                                voz.append(Nota("-", bpm, vol[i], inst[i]))
                                ultimo_char_nota = False
                        elif ultimo_char_nota:
                            voz.append(voz[-1])
                            ultimo_char_nota = False
                        
            self.partitura.append(voz)


