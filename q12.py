# O objetivo dessa questão é verficar o polimorfismo com Python.
# Percebemos que cada classe Gestor, Estagiário e Analista
# tem implementações distintas para o método calcular_bonus.
# Além disso, o método adicionar pode ser usado tanto para o
# login, quanto ao somar valores, mostrando a utilidade do
# Duck Typing


class Funcionario:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario

    @staticmethod
    def adicionar(a, b):
        return a+b

    def login(self):
        return self.adicionar(self.nome, self.sobrenome)


class Gestor(Funcionario):
    def calcular_bonus(self):
        return self.salario*4


class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.adicionar(self.salario, 600)


class Analista(Funcionario):
    def calcular_bonus(self):
        return self.salario*3


print("\nEstagiário")
estag = Estagiario("Joao", "Silva", 1000)
print("Bônus: ", estag.calcular_bonus(),
      "\nLogin: ", estag.login())

print("\nGestor")
gest = Gestor("Maria", "Rosa", 11000)
print("Bônus: ", gest.calcular_bonus(),
      "\nLogin: ", gest.login())