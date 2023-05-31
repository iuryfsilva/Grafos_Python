notas_disponiveis = [200, 100, 50, 10]
    
def calcular_notas(saque):
    notas_saque = [0, 0, 0, 0]

    for i, nota in enumerate(notas_disponiveis):
        while saque >= nota:
            saque -= nota
            notas_saque[i] += 1

    return notas_saque

def main():
    valor_minimo = 10
    valor_maximo = 1000
    valor_multiplo = 10

    # Solicitar valor do saque ao usuário
    saque = int(input("Digite o valor do saque (múltiplo de 10): "))

    # Verificar se o valor está dentro dos limites permitidos
    if saque < valor_minimo or saque > valor_maximo or saque % valor_multiplo != 0:
        print("Valor de saque inválido.")
    else:
        notas_saque = calcular_notas(saque)

        # Exibir quantidade de notas de cada valor
        print("Notas fornecidas:")
        for i, nota in enumerate(notas_saque):
            if nota > 0:
                print(f"{nota} nota(s) de R${notas_disponiveis[i]}")

if __name__ == '__main__':
    main()