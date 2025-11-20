#Escreva um programa que utilize o conceito de execução condicional, use uma string como entrada e:
#imprime a frase "Sim - Spathiphyllum é a melhor
#fábrica de todos os tempos!" para a tela se a sequência inserida for "Spathiphyllum" (maiúscula)
#imprime "Não, eu quero um grande Spathiphyllum!" se a sequência inserida for "spathiphyllum" (letra minúscula)
#imprime "Spathiphyllum! Not[input]!", Caso contrário. Nota: [input] é a string usada como entrada.

user_string = input("Informe a string: ")

if user_string == "Spathiphyllum":
    print("Sim - Spathiphyllum eh a melhor")
elif user_string == "spathiphyllum":
    print("Nao, eu quero uma grande Spathiphyllum")
else: 
    print("Spathiphyllum! Not ", user_string)