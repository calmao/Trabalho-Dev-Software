import musica
import sys
import mido

    
def main():
    vol = [100]
    oitava = [3]
    inst = [0]
    bpm = 100

    
    p = musica.Interpretador()
    p.transcrever(sys.argv[1], bpm, inst, vol, oitava)
    
    #print(mido.get_output_names()[0])

    m = musica.Musica()
    m.iniciar(p)
    print(m)
    #m.tocar()

    return
main()