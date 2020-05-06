# Objetivo: criar um programa que ilustre o uso de métodos
# abstratos, métodos de classe e métodos estáticos, mostrando
# as vantagens de cada tipo de método.

# Métodos abstratos podem ser usados quando queremos que uma
# classe filha obrigatoriamente implemente esse método. Por
# exemplo, vamos considerar a classe PoligonoRegular. Implementamos
# o método abstrato get_area. Assim, a classe quadrado também deve
# implementar esse método

# Métodos estáticos são úteis ao implementar algo relacionado à
# classe, mas não exatamente a um objeto específico. Por exemplo,
# vamos supor que temos uma variável de classe que conta quantos
# PoligonosRegulares foram criados. O método que retorna esse valor
# pode ser um método estático. Além disso, se formos criar um método
# que não depende do objeto instanciado, esse método pode ser
# estático (como por exemplo, o método calcula_angulo_interno)

# Métodos de classe são aqueles que necessitam de objeto instanciado.
# Por exemplo, o método get_area


import abc


class PoligonoRegular(object):
    __metaclass__ = abc.ABCMeta
    quantidade = 0

    def __init__(self):
        PoligonoRegular.quantidade += 1

    @abc.abstractmethod
    def get_area(self):
        """ Retorna a área do Pol[gono"""

    @staticmethod
    def calcular_angulo_interno(l):
        return 180 * (l - 2) / l

    @staticmethod
    def get_quantidade():
        return PoligonoRegular.quantidade


class Quadrado(PoligonoRegular):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.angulo_interno = self.calcular_angulo_interno(lado)

    def get_area(self):
        return self.lado ** 2


a = Quadrado(2)
print("Quatidade polígonos: ", PoligonoRegular.get_quantidade())
b = Quadrado(3)
print("Quantidade de polígonos: ", PoligonoRegular.get_quantidade())

print("Área quadrado b: ", b.get_area())
