# Nessa questão criamos um decorador que calcula o tempo
# de execução das funções e imprime alguns comentários.

import time


def decorador_calculadora(func_calc):
    def decorador(calculator):
        print("Efetuando operação: ", func_calc.__name__)
        start = time.time()
        print(func_calc(calculator))
        end = time.time()
        print("Calculo terminado. Temṕo: ", end - start)
        print('\n')

    return decorador


class Calculadora:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @decorador_calculadora
    def soma(self):
        return self.x + self.y

    @decorador_calculadora
    def multiplicacao(self):
        return self.x * self.y


a = Calculadora(10, 11)
a.soma()
a.multiplicacao()