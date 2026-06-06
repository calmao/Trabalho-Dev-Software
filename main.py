import musica
import sys
import mido

    
def main():
    vol = [100, 100]
    oitava = [4, 3]
    inst = [0, 0]
    bpm = 60

    
    p = musica.Interpretador()
    p.transcrever(sys.argv[1], bpm, inst, vol, oitava)
    
    #print(mido.get_output_names()[0])

    m = musica.Musica()
    m.iniciar(p)
    print(m.mid.length)
    #print(m.mid.tracks)
    #m.tocar()

    return
main()