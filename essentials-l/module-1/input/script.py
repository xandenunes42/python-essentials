leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)


#concatenação de strings
fnam = input("Informe o primeiro nome, por favor? ")
lnam = input("Informe o seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")