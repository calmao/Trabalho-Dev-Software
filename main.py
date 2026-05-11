import transcrever
import sys

    
def main():
    inst = [100, 115, 15]
    bpm = [100, 100, 100]

    p = transcrever.transcrever(sys.argv[1], bpm, inst)

    print(p)

    return
main()