# Trabalho-Dev-Software

## Download e Utilização
	- Feito em Python 3.12.10
	- Programa exige as bibliotecas : mido[mido-rtmidi], tkinter e pygame
	- Para abrir a interface e utilizar o programa basta abrir um terminal no root do programa e chamar:
		$ python3 main.py 


## Boas práticas
	- Variaveis em snake_case

## Como usar os Módulos Música e Interpretador
	p.trancrever("nome_do_arquivo.txt", bpm, instrumento) - implementado
	//vai transcrever as informações da arquivo para a partitura

	m.iniciar(p) - implementado
	//vai transformar as informações contidas no interpretador p em mensagens MIDI
	m.tocar()
	//toca a musica

	m.salvar() - implementado
	//salva a musica em um arquivo MIDI

## Módulos

- Trancrição: transforma o txt em um formato intermediário
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


