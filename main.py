import musica
import sys

    
def main():
    vol = [0, 0, 0]
    oitava = [0, 0, 0]
    inst = [100, 115, 15]
    bpm = 100

    p = musica.Interpretador()
    p.transcrever(sys.argv[1], bpm, inst, vol, oitava)

    print(p)

    m = musica.Musica()

    m.iniciar(p)

    return
main()