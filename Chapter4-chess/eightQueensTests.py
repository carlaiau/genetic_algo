import unittest
import datetime
import genetic

class EightQueensTests(unittest.TestCase):

    def main(self, size = 30):
        geneset = [i for i in range(size)]

        def fnDisplay(candidate):
            display(candidate, size)

        def fnGetFitness(genes):
            return get_fitness(genes, size)

        optimalFitness = Fitness(0)

        best = genetic.get_best(fnGetFitness, 2 * size, optimalFitness,
                                geneset, fnDisplay)

        self.assertTrue(not optimalFitness > best.Fitness)

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.main(20))


class Board:

    def __init__(self, genes, size):
        board = [['.'] * size for _ in range(size)]

        for index in range(0, len(genes), 2):
            row = genes[index]
            column = genes[index + 1]
            board[column][row] = 'Q'

        self._board = board

    def get(self, row, column):
        return self._board[column][row]

    def print(self):
        for i in reversed(range(0, len(self._board))):
            print(' '.join(self._board[i]))


def display(candidate, size):

    board = Board(candidate.Genes, size)
    board.print()
    print("{}\tFitness: {}".format(
        ' '.join(map(str, candidate.Genes)),
        candidate.Fitness))

# Override Fitness
class Fitness:

    def __init__(self, total):
        self.Total = total

    def __gt__(self, other):
        return self.Total < other.Total

    def __str__(self):
        return "{}".format(self.Total)


def get_fitness(genes, size):
    board = Board(genes, size)
    rowsWithQueens = set()
    colsWithQueens = set()

    northEastQueens = set()
    southEastQueens = set()

    for row in range(size):
        for col in range(size):
            if board.get(row, col) == 'Q':
                rowsWithQueens.add(row)
                colsWithQueens.add(col)
                northEastQueens.add(row + col)
                # Review first principles math for this
                southEastQueens.add(size - 1 - row + col )

    total = (
        size - len(rowsWithQueens) +
        size - len(colsWithQueens) +
        size - len(northEastQueens) +
        size - len(northEastQueens))

    return Fitness(total)



if __name__ == '__main__':
    unittest.main()