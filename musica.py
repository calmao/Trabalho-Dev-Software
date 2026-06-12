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
                    track.append(Message('note_on', channel=i, note=c.freq, velocity=c.vol, time=int(tempo)))
                    track.append(Message('note_off', channel=i, note=c.freq, velocity=c.vol, time=int(cons_t/c.bpm)))
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
            

