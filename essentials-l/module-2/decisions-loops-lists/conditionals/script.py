#if true_or_not:
#   do_this_if_true

sheep_counter = 130

if sheep_counter >= 120: # Avaliar uma expressão de teste
    print("sleep_and_dream") # Execute se a expressão de teste for verdadeira
 
#else 

#if true_or_false_condition:
#   perform_if_condition_true
#else:
#   perform_if_condition_false


#if-else aninhados 
the_weather_is_good = False
tickets_are_available = False

if the_weather_is_good:
    if nice_restaurant_is_found:
        print("have_lunch")
    else:
        print("eat a sandwich")
else:
    if tickets_are_available:
        print("go to the teather")
    else:
        print("go shopping")

#elif
table_is_available = True

if the_weather_is_good:
    print("go for a walk")
elif tickets_are_available:
    print("go to the teather")
elif table_is_available:
    print("go for lunch")
else:
    print("play chess at home")




#Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# verificar número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)


#FUNÇAO MAX -> ENCONTRA O MAIOR NUMERO
# Leia três números.
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
 
largest_number = max(number1, number2, number3)
 
# Imprimir o resultado.
print("O maior número é:", largest_number)
 

 

 

