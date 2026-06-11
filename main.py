from musica import Musica
from interpretador import Interpretador
import sys
import mido
import time
import classe_interface as ui

    
def main():
<<<<<<< HEAD
    vol = [100, 100]
    oitava = [4, 3]
    inst = [0, 34, 117]
=======
    '''
    vol = [100,100]
    oitava = [4,3]
    inst = [127,127]
>>>>>>> 4940652244e293a916f5ba9bbfe8d69b9307ff1d
    bpm = 60

    
    p = Interpretador()
    p.transcrever(sys.argv[1], bpm, inst, vol, oitava)
    
    #print(mido.get_output_names()[0])

    m = Musica()
    m.iniciar(p)
    #print(m.mid.length)
    #print(m.mid.tracks)
<<<<<<< HEAD
    m.tocar()
    #m.tocar()
    #m.salvar('doremifa.mid')
=======
    #m.tocar()
    m.salvar('doremifa.mid')'''

    interface = ui.InterfaceGrafica()
    interface.mainloop()
>>>>>>> 4940652244e293a916f5ba9bbfe8d69b9307ff1d

    return
main()