my_list = [8,10,4,2,9,6]

swapped = True

while swapped:
    swapped = False

    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            swapped = True
            #se nada acontece, swapped foi desativado no inicio do ciclo, logo, encerra

print(my_list)


my_list2 = [84, 10, 62, 23, 45]
my_list2.sort() # metodo para ordenar indices em ordem crescente
my_list2.reverse() #inverte a ordem dos indices, do maior pro menor 
print(my_list2)
 

