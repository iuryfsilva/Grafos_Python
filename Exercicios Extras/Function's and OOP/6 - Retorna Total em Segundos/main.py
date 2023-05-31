def converteTempoParaSegundos(dias, horas, minutos, segundos):
    return (((((dias * 24) + horas) * 60) + minutos) * 60) + segundos

dias = int(input("Informe o numero de dias: ")) 
horas = int(input("Informe o numero de horas: ")) 
minutos = int(input("Informe o numero de minutos: ")) 
segundos = int(input("Informe o numero de segundos: ")) 

print("Tempo informado em segundos = " + str(converteTempoParaSegundos(dias, horas, minutos, segundos)))