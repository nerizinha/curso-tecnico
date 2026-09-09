saldo = 500
saque = int(input("digite o valor do saque:"))
if saque <= saldo:
    print("saque realizado com sucesso!")
else:
    print("saldo insuficiente!")