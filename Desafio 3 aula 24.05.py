salario = float(input("Novo salário do funcionário: "))

if salario > 8250.00:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print("O valor do aumento é", novo_salario)