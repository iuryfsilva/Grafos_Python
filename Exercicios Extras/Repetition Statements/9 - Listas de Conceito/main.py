conceitoA = []
conceitoB = []
conceitoC = []
conceitoD = []
conceitoE = []

while True:
    nota = float(input("Informe a nota: ")) 
    if nota != (-1):
        if nota >= 9.0 and nota <= 10.0:
            conceitoA.append(nota)
        elif nota >= 8.0 and nota < 9.0:
            conceitoB.append(nota)
        elif nota >= 7.0 and nota < 8.0:
            conceitoC.append(nota)
        elif nota >= 6.0 and nota < 7.0:
            conceitoD.append(nota)
        elif nota >= 0.0 and nota <= 6.0:
            conceitoE.append(nota)
    else:
        break

print("Conceito A: " + str(conceitoA) + "\nConceito B: " + str(conceitoB) + "\nConceito C: " + str(conceitoC) + "\nConceito D: " + str(conceitoD) + "\nConceito E: " + str(conceitoE))
