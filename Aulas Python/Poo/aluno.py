class Aluno:
	def __init__(self, nome, idade, nota, freq):# Construtor da classe
		self.nome = nome
		self.idade = idade
		self.nota = nota
		self.freq = freq

	def aprovado():
		if self.nota>=6 and self.freq >=0.75:
			return True
		else:
			return false