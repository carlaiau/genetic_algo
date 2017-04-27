import random
import datetime
import genetic
import unittest


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}\t".format(
        ''.join(candidate.Genes),
        candidate.Fitness,
        timeDiff))


class GuessPasswordTests(unittest.TestCase):

    geneset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! "

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(''.join(best.Genes), target)


    def test_Random(self):
        length = 15
        target = ''.join(random.choice(self.geneset)
                         for _ in range(length))

        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)


if __name__ == '__main__':
    unittest.main()

