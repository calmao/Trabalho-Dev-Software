class Nota:
    def __init__(self, freq, bpm, vol, inst):
        self.freq = freq
        self.bpm = bpm
        self.vol = vol
        self.inst = inst
    
    def __str__(self):
        return f"{self.freq}"

def transcrever(nome_arquivo, bpm, inst): # (str, list[float], list[int], list[int], list[int])

    vol = []
    oitava = []

    arq = open(nome_arquivo)
    partitura = []
    
    for i in range(len(inst)):
        oitava_ini = 6-(i%7)
        ultimo_char_nota = False #verdadeiro se, e somente se o ultimo caracter lido for uma nota
        
        oitava.append(oitava_ini)
        vol.append(100 - (20*i))

        voz = []
        l = arq.readline()

        a = 0
        if l[0] == "[":
            a = int(l[1:l.rfind("]")])
            for i in range(a):
                voz.append(Nota("-", bpm[i], vol[i], inst[i]))
        
        for j in range(a, len(l)):
            ultimo_char_nota = False
            match l[j]: #primeiro switch/case case trata de ações, se cair no default entra no switch/case de notas
                
                case "!":
                    inst[i] = 24
                case "I" | "i" | "O" | "o" | "U" | "u":
                    inst[i] = 110
                case ";" | "1" | "3" | "5" | "7" | "9":
                    inst[i] = 15
                case "0":
                    inst[i] = inst[i]
                case "2":
                    inst[i] = inst[i] + 2
                case "4":
                    inst[i] = inst[i] + 4
                case "6":
                    inst[i] = inst[i] + 6
                case "8":
                    inst[i] = inst[i] + 8
                case "?":
                    oitava[i] += 1
                    if oitava[i] ==10:
                        oitava[i]= oitava_ini
                case "V":
                    oitava[i] -= 1
                    if oitava[i] == 0:
                        oitava[i]= oitava_ini
                case ">":
                    bpm[i] += 10
                case "<":
                    bpm[i] -= 10
                case " ":
                    vol[i] = 2*vol[i]
                    if vol[i] > 127:
                        vol[i] = 127
                case _:
                    if (ord(l[j]) > 64 and ord(l[j]) < 73):
                        voz.append(Nota(f"{l[j]}{oitava[i]}", bpm[i], vol[i], inst[i]))
                        ultimo_char_nota = True
                    elif (ord(l[j]) > 96 and ord(l[j]) < 105):
                        if(l[j] != "b" or l[j-1] != "M"):
                            voz.append(Nota("-", bpm[i], vol[i], inst[i]))
                    elif l[j] == "M":
                        voz.append(Nota("M"+str(oitava[i]), bpm[i], vol[i], inst[i]))
                    elif ultimo_char_nota:
                        voz.append(voz[-1])
                    
        partitura.append(voz)

    arq.close()
    return partitura

