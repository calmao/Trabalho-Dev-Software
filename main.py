from musica import Musica
from interpretador import Interpretador
import sys
import mido
import time
import classe_interface as ui

    
def main():
   """Inicializa e exibe a interface gráfica da aplicação."""
   interface = ui.InterfaceGrafica()
   interface.mainloop()
   
   return
main()
