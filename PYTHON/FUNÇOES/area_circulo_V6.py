#FAZENDO RETURN DA FORMULA DsA AREA DO CIRCULO

from math import pi


def circulo(raio):
    return pi * raio**2



if __name__ == '__main__':
    raio = float(input("Digite o raio do circulo: "))
    area = circulo(raio)
    print (f'Area do circulo {area :.2f}')