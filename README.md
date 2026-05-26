# Trabalho-Dev-Software

## Módulos

- Transcrição: transforma o .txt em um formato intermediário
- Intreface: interage com o usuário (Toca o arquivo MIDI) [pygame]
- Música: transforma o intermediário em um arquivo MIDI [MIDO]


## Transcrição

Definição do Formato Intermediário:

	Classe Partitura:
		- Lista de Listas de Notas
		
	Classe Nota:
		- Frequencia (nota e oitava)
		- BPM (floats)
		- Volume (int entre 0 e 127)
		- Instrumento (int)


