# Trabalho-Dev-Software

## Boas práticas
	- Variaveis em snake_case

## Como usar os Módulos Música e Trancrição
	p = trancrever("nome_do_arquivo.txt", bpm, instrumento) - implementado
	//retorna a partitura p após recebe o arquivo txt e as listas de bpm e instrumentos iniciais de cada voz

	tocar(p) - não implementado
	//toca a partitura p

	salvar(p) - não implementado
	//salva o arquivo MIDI de p

## Módulos

- Trancrição: transforma o txt em um formato intermediário
- Intreface: interage com o usuário [pygame]
- Música: transforma o intermediário em um arquivo MIDI e o toca[MIDO]


## Transcrição

Definição do Formato Intermediário:

	Classe Partitura:
		- Lista de Listas de Notas
		
	Classe Nota:
		- Frequencia (nota e oitava)
		- BPM (floats)
		- Volume (int entre 0 e 127)
		- Instrumento (int)


