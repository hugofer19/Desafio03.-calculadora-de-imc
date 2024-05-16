print("Calculadora de Índice de Massa Corporal")
peso = float(input("Escreva o seu peso: "))
altura = float(input("Escreva a sua altura: "))

imc = peso/(altura*altura)

print("O seu Índice de Massa Corporal (IMC) é de:", str(imc))
