from musica import Musica
from interpretador import Interpretador
import sys
import mido
import time

    
def main():
    vol = [100, 100]
    oitava = [4, 3]
    inst = [0, 34, 117]
    bpm = 60

    
    p = Interpretador()
    p.transcrever(sys.argv[1], bpm, inst, vol, oitava)
    
    #print(mido.get_output_names()[0])

    m = Musica()
    m.iniciar(p)
    print(m.mid.length)
    #print(m.mid.tracks)
    m.tocar()
    #m.tocar()
    #m.salvar('doremifa.mid')

    return
main()