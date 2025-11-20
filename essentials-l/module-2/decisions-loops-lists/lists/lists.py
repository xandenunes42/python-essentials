lista = [1,2,3,4,5,6,7,8,9]

#indexando elementos
lista[0] = lista[8]

for i in lista:
    print(i, end=" ")
# print(lista)

#funcao len
print("\n", len(lista))
#retorna o tamanho da lista -> 9


#remover elementos
del lista[0]
print("\n", len(lista))


#indices negativos sao permitidos
print(lista[-1]) 
# -1 retorna o ultimo elemento da lista
# -2 retorna o penultimo elemento da lista

#adicionando elementos
#append() e insert()

lista.append(99)
#adiciona valor no fim da lista

lista.insert(0, 1)
#adiciona -> insert(location, valor)


my_list = [] # Criando uma lista vazia.

for i in range(5):
   my_list.append(i + 1)

print (my_list)

my_list = []  # Criando uma lista vazia.

for i in range(5):
    my_list.insert(0, i + 1)
#elementos sao adicionados e deslocados para direita
print(my_list)