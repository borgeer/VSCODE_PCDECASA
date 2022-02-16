peso = float(input("Peso que Joao pescou: "))

if peso <= 50.0:
    print("Joao não paga multa")

if peso > 50.0:
    ex = peso-50
    multa= ex*4
    print(f'Joao execedeu em {ex}KG e ira pagar R${multa:.2f} de multa')