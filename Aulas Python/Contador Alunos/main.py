Aprovados = 0
notas = [[4,6,8], [9,2,7], [10,5,9]]
for i in range(len(notas)):
	for j in range(len(notas[i])):
		if notas[i][j] >= 6:
			Aprovados = Aprovados + 1

print(Aprovados)
