import musica
import sys

    
def main():
    inst = [100, 115, 15]
    bpm = 100

    p = musica.transcrever(sys.argv[1], bpm, inst)

    for i in p:
        for j in i:
            print(j, end="")
        print("")

    return
main()