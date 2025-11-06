'''
Cenário
Era uma vez uma terra - uma terra de leite e mel, habitada por pessoas felizes e prósperas. 
As pessoas pagavam impostos, é claro - a felicidade tinha limites. O imposto mais importante, 
chamado de imposto de renda pessoal (PIT) tinha que ser pago uma vez por ano e foi avaliado 
usando a seguinte regra:

se a renda do cidadão não era superior a 85.528 talões, o imposto era igual a 18% da renda, 
menos 556 taller e 2 centavos (isso era o que eles chamavam de isenção de imposto)
se a receita fosse superior a esse valor, o imposto seria igual a 14.839 talões e 2 centavos, 
mais 32% do excedente em mais de 85.528 taller.

Sua tarefa é escrever uma calculadora de impostos.

Ela deve aceitar um valor de ponto flutuante: a receita.
Em seguida, ele deve imprimir o imposto calculado, arredondado para inteiro. 
Há uma função chamada round() que fará o arredondamento para você - 
você a encontrará no código do esqueleto no editor.

Nota: esse país feliz nunca devolveu dinheiro para seus cidadãos. 
Se o imposto calculado for menor que zero, isso significaria apenas nenhum imposto 
(o imposto foi igual a zero). Leve isso em consideração durante os cálculos.
'''

tax = 85528
#tax = imposto de renda

income = float(input("Informe o valor da receita: "))
#income = receita

if income <= 0:
    print("Informe valor maior que zero!!!")
elif income > tax:
    increse = 0.32
    surplus = income - tax
    toDeclare = int((surplus * increse) + 14839.02)
    print(round(toDeclare, 0))
else:
    discount = 0.18
    toDeclare = int((income * discount) - 556.02)
    
    if toDeclare <= 0:
        print("Nao sera necessaria a declaracao de impostos")

    else:
        print(round(toDeclare, 0))