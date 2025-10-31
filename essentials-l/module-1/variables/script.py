# Esse programa calcula a hipotenusa c.
# a e b são os tamanhos dos lados.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # Nós usamos ** ao invés de raiz quadrada.
print("c =", c)

#Conversor de milhas para quilometros 

kilometers = 12.25
miles = 7.38

miles_to_kilometers = 1.6 * miles
kilometers_to_miles = kilometers / 1.6

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")

quilometros = 10
milhas = 3.4

milhas_para_quilometros = milhas * 1.6
quilometros_para_milhas = quilometros / 1.6

print("milhas: ", milhas, "quilometros: ", round(milhas_para_quilometros, 2))
print("quilometros: ", quilometros, "milhas: ", round(quilometros_para_milhas, 2 ))


x = 0


y = float((3 * (x ** 3)) - (2 * (x ** 2)) + 3 * x - 1)

print(y)


x = 11
y = 4
 
x = x % y
x = x % y
y = y % x
 
print(y)
 
