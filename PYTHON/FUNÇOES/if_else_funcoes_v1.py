

def nota(valor):
    if valor > 10 or valor < 0:
        return 'Nota inválida'
    if valor <= 10 and valor >= 9.1:
        return 'A'
    if valor <= 9.0 and valor >= 8.1:
        return "A-"
    if valor <= 8.0 and valor >= 7.1:
        return "B"
    if valor <= 7.0 and valor >= 6.1:
        return "b-"
    if valor <= 6.0 and valor >= 5.1:
        return "C"
    if valor <= 5.0 and valor >= 4.1:
        return "C-"
    if valor <= 4.0 and valor >= 3.1:
        return "D"
    if valor <= 3.0 and valor >= 2.1:
        return "D-"
    if valor <= 2.0 and valor >= 1.1:
        return "E"
    if valor <= 1.0 and valor >= 0.0:
        return "E-"


if __name__ == '__main':
    valor_informado = float(input("Digite a nota: "))
    conceito = nota(valor_informado)

    print(conceito)
