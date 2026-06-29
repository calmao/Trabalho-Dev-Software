from mido import  Message, MidiFile, MidiTrack
import mido
import time
from interpretador import Interpretador
import pygame


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
        for indice_voz, voz in enumerate(trancricao.partitura):
            track = MidiTrack()
            track.append(Message('program_change', channel=indice_voz, program=voz[0].inst, time=0))
            inst_anterior = voz[0].inst
            for nota in voz:
                if (nota.freq == -1):
                    tempo += cons_t/nota.bpm
                else:
                    if(inst_anterior != nota.inst):
                        inst_anterior = nota.inst
                        track.append(Message('program_change', channel=indice_voz, program=nota.inst, time=0))
                    track.append(Message('note_on', channel=indice_voz, note=nota.freq, velocity=nota.vol, time=int(tempo)))
                    track.append(Message('note_off', channel=indice_voz, note=nota.freq, velocity=nota.vol, time=int(cons_t/nota.bpm)))
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

    def tocar_arquivoMIDI(self,nomeDoMidi):
        pygame.init()
        pygame.mixer.music.load(nomeDoMidi)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(1000)
    
            

