from musica import Musica
from interpretador import Interpretador
import sys
import mido
import time
import classe_interface as ui

    
def main():
    '''
    vol = [100,100]
    oitava = [4,3]
    inst = [127,127]
    bpm = 60

    
    p = Interpretador()
    p.transcrever(sys.argv[1], bpm, inst, vol, oitava)
    
    #print(mido.get_output_names()[0])

    m = Musica()
    m.iniciar(p)
    #print(m.mid.length)
    #print(m.mid.tracks)
    #m.tocar()
    m.salvar('doremifa.mid')'''

    interface = ui.InterfaceGrafica()
    interface.mainloop()

    return
main()