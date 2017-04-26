import random
import datetime
import genetic
import unittest

class GuessPasswordTests(unittest.TestCase):

    geneset = "1234567890 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,'()/?"

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_Lipsum(self):
        target= "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        self.guess_password(target)

    def guess_password(self, target):
        geneSet = "1234567890 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,'()/?"
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return self.get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)

        self.assertEqual(best.Genes, target)

    def get_fitness(self,genes, target):
        return sum(1 for expected, actual in zip(target, genes)
                    if expected == actual)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Hello_World)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print( "{}\t{}\t{}\t".format(candidate.Genes, candidate.Fitness, timeDiff))



if __name__ == '__main__':
    unittest.main()

