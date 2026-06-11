import pygame

def tocar_arquivoMIDI(nomeDoMidi):
   
    pygame.init()
    pygame.mixer.music.load(nomeDoMidi)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)
    

