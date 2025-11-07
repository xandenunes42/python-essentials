"""
import time

for i in range(100):
    # do_something()
    pass # a instrução for necessita ao menos uma instrucao no corpo (o msm para while, if, elif)
 
# i: variavel de controle do loop (as voltas do loop)
# in: define o "universo" de valores que a variável de controle vai percorrer. 
    # for variavel_controle in sequencia:
    # bloco de código

for i in range(10):
   print("O valor de i é atualmente", i)

# o loop foi executado dez vezes (é o argumento da função range())

# Escreva um loop for que conte até cinco
for i in range(1, 6):
   # Corpo do loop - exiba o número de iteração do loop e a palavra "Mississippi".
   print(f"{i} mississippi.")
   # Corpo do loop - use: time.sleep(1)
   time.sleep(1)
# Escreva uma função print com a mensagem final.
print("Fim do loop.")



# break - sai do loop imediatamente e termina incondicionalmente a operação do loop; 
# o programa começa a executar a instrução mais próxima após o corpo do loop;

# continue - se comporta como se o programa tivesse chegado ao fim do corpo; 
# o próximo turno é iniciado e a expressão de condição é testada imediatamente.


# break - exemplo

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")


# continue - exemplo

print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")
"""

nome = input("Informe o nome:\n")
nome = nome.upper()

for i in nome:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        continue
    else:
        print(i)