import mido
import time

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
    
    def __str__(self):
        s = ''
        for i in self.partitura:
            for j in i:
                s += j.freq
            s += '\n'
        return str(s)

    def transcrever(self, nome_arquivo, bpm, inst, vol, oitava): # (str, list[float], list[int], list[int], list[int])
        if (bpm == -1):
            bpm = 100

        arq = open(nome_arquivo)
        for i in range(len(inst)):
            match(i%4):
                case 0:
                    if(inst[i] == -1):
                        inst[i] = 0
                    if(vol[i] ==-1):
                        vol[i] = 100
                    if(oitava[i] == -1):
                        oitava[i] = 6
                case 1:
                    if(inst[i] == -1):
                        inst[i] = 20
                    if(vol[i] ==-1):
                        vol[i] = 80
                    if(oitava[i] == -1):
                        oitava[i] = 5
                case 2:
                    if(inst[i] == -1):
                        inst[i] = 6
                    if(vol[i] ==-1):
                        vol[i] = 60
                    if(oitava[i] == -1):
                        oitava[i] = 4
                case 3:
                    if(inst[i] == -1):
                        inst[i] = 71
                    if(vol[i] ==-1):
                        vol[i] = 40
                    if(oitava[i] == -1):
                        oitava[i] = 5
        
        for i in range(len(inst)):
            ultimo_char_nota = False #verdadeiro se, e somente se, o ultimo caracter lido for uma nota
            oitava_ini = oitava[i]

            voz = []
            l = arq.readline()

            a = 0
            if l[0] == "[":
                a = int(l[1:l.rfind("]")])
                for i in range(a):
                    voz.append(Nota("-", bpm, vol[i], inst[i]))
            
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
                        if oitava[i] == -2:
                            oitava[i]= oitava_ini
                    case ">":
                        bpm += 10
                    case "<":
                        bpm -= 10
                    case " ":
                        vol[i] = 2*vol[i]
                        if vol[i] > 127:
                            vol[i] = 127
                    case _:
                        if (ord(l[j]) > 64 and ord(l[j]) < 73):
                            voz.append(Nota(f"{l[j]}{oitava[i]}", bpm, vol[i], inst[i]))
                            ultimo_char_nota = True
                        elif (ord(l[j]) > 96 and ord(l[j]) < 105):
                            if(l[j] != "b" or l[j-1] != "M"):
                                voz.append(Nota("-", bpm, vol[i], inst[i]))
                        elif l[j] == "M":
                            voz.append(Nota("M"+str(oitava[i]), bpm, vol[i], inst[i]))
                        elif ultimo_char_nota:
                            voz.append(voz[-1])
                        
            self.partitura.append(voz)

        arq.close()

class Musica:
    def __init__(self):
        self.estado = "Parado"
        self.posicao = -1

    def __str__(self):
        return str(self.mid.tracks[0])

    def iniciar(self, trancricao:Interpretador):
        cons_t = 14400
        mido.set_backend('mido.backends.rtmidi')
        tempo = 0
        self.mid = mido.MidiFile(type=1)
        for voz in trancricao.partitura:
            track = mido.MidiTrack()
            for c in voz:
                if (c.freq == '-'):
                    tempo += cons_t/c.bpm
                else:
                    nota = (int(c.freq[1]) + 1)*12
                    match(c.freq[0]):
                        case 'C':
                            nota += 0
                        case 'D':
                            nota += 2
                        case 'M':
                            nota += 3
                        case 'E':
                            nota += 4
                        case 'F':
                            nota += 5
                        case 'G':
                            nota += 7
                        case 'A':
                            nota += 9
                        case 'H':
                            nota += 10
                        case 'B':
                            nota += 11
                    track.append(mido.Message('note_on', note=nota, velocity=c.vol, time=tempo))
                    track.append(mido.Message('note_off', note=nota, velocity=c.vol, time=cons_t/c.bpm))
                    tempo = 0
            self.mid.tracks.append(track)
    
    def tocar(self):
        with mido.open_output(mido.get_output_names()[0]) as self.port:
            self.estado = 'tocando'
            time.sleep(0.5)
            for msg in self.mid.play():
                if(self.estado != 'tocando'):
                    break
                self.port.send(msg)
            time.sleep(0.5)
            

