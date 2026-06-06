from mido import  Message, MidiFile, MidiTrack
import mido
import time
from interpretador import Interpretador


class Musica:
    def __init__(self):
        self.iniciada = False
        self.tocando = False
        self.posicao = -1

    def __str__(self):
        return str(self.mid.tracks[0])

    def iniciar(self, trancricao:Interpretador):
        self.iniciada = True
        cons_t = 14400
        mido.set_backend('mido.backends.rtmidi')
        tempo = 0
        self.mid = MidiFile(type=1)
        for i, voz in enumerate(trancricao.partitura):
            track = MidiTrack()
            track.append(Message('program_change', channel=i, program=voz[0].inst, time=0))
            inst_anterior = voz[0].inst
            for c in voz:
                if (c.freq == '-'):
                    tempo += cons_t/c.bpm
                else:
                    if(inst_anterior != c.inst):
                        inst_anterior = c.inst
                        track.append(Message('program_change', channel=i, program=c.inst, time=0))
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
                    track.append(Message('note_on', channel=i, note=nota, velocity=c.vol, time=int(tempo)))
                    track.append(Message('note_off', channel=i, note=nota, velocity=c.vol, time=int(cons_t/c.bpm)))
                    tempo = 0
            self.mid.tracks.append(track)
    
    def tocar(self):

        if(self.iniciada):
            with mido.open_output(mido.get_output_names()[0]) as self.port:
                self.tocando = True
                time.sleep(0.5)
                for msg in self.mid.play():
                    if(not self.tocando):
                        break
                    self.port.send(msg)
                time.sleep(0.5)
    
    def parar(self):
        self.tocando = False

    def salvar(self, nome):
        self.mid.save('Saidas/' + nome)
            

