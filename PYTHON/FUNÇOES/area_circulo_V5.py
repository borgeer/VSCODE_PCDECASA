#FAZENDO UMA FUNÇAO PARA A FORMULA DA AREA DO CIRCULO 

from math import pi


def circulo(raio):
    areac = pi * raio**2
    print(f' A area do circulo é de {areac :.2f}')


if __name__ == '__main__':
    raio = float(input("Digite o raio do circulo: "))
    circulo(raio)