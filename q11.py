# Objetivo: criar um exemplo de função com lista de
# argumentos e dicionário de argumentos


def printar_comentario_prova(acertos, professor, *args, **kwargs):
    print('*' * 30)
    for chave, valor in kwargs.items():
        print(chave, ":", valor)

    print("\nSua nota foi: ", acertos, ". Comentários:")

    for arg in args:
        print(arg)

    print("\nAtt,")
    print(professor)
    print('*' * 30)


aluno = {
    'Nome': 'João',
    'Sobrenome': 'da Silva',
    'Turma': 'ITA'
}

erros = {
    'Questão 1: faltou terminar', 'Questão 5: multiplicou errado', 'Questão 9: em branco'
}

professor = "Maria"

printar_comentario_prova(7, professor, *erros, **aluno)