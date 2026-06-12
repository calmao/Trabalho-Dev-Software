from musica import Musica
from interpretador import Interpretador
import sys
import mido
import time
import classe_interface as ui

    
def main():
    '''
    vol = [100,100, 100]
    inst = [127,0, 3]
    bpm = 60

    a = open(sys.argv[1])
    s = a.read()
    a.close()
    p = Interpretador()
    p.transcrever(s, bpm, inst, vol)
    for i in p.partitura:
        for j in i:
            print(j.inst, end='')
        print('')

    #print(mido.get_output_names()[0])

    #m = Musica()
    #m.iniciar(p)
    #print(m.mid.length)
    #print(m.mid.tracks)
    #m.tocar()
    #m.salvar('doremifa.mid')
    '''

    interface = ui.InterfaceGrafica()
    interface.mainloop()

    return
main()