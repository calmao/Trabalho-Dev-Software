import pygame

pygame.init()
pygame.mixer.init()

def tocar_arquivoMIDI(nomeDoMidi):
    pygame.mixer.music.load(nomeDoMidi)
    pygame.mixer.music.play()


def pausar_arquivoMIDI():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()


def despausar_arquivoMIDI():
    pygame.mixer.music.unpause()


def parar_arquivoMIDI():
    pygame.mixer.music.stop()

