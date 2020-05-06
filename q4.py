# Nesse exercício modificamos o problema da rainha do livro
# para resolver qualquer tamanho de tabuleiro

import random
import time


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy  # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False  # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def find_some_solutions(size_board):
    rng = random.Random()  # Instantiate a generator
    bd = list(range(size_board))  # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1


print("Size Puzzle = 4")
find_some_solutions(4)
print("\nSize Puzzle = 12")
find_some_solutions(12)

# We can check the time need to find 10
# solutions for a fixed puzzle size
print("\nSize Puzzle = 16")
start = time.time()
find_some_solutions(15)
end = time.time()
print(end - start)

# No meu computador, o tempo para achar 10 soluções
# para tamanho de tabuleiro 16 está geralmente
# entre 1 e 2 minutos. Podemos ver que para tamanho
# 12 é bem rápido. Assim, o maior tamanho de tabuleiro
# que pode ser resolvido em menos de um minuto
# é provavelmente 15.