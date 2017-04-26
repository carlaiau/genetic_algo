import random
import datetime
import genetic
import unittest

class GuessPasswordTests(unittest.TestCase):

    geneset = "1234567890 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,'()/?"

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_Thaddeus(self):
        target= "Haven't been doing much ae. Course starts in 3 weeks. Will have to get into some study to prepare"
        self.guess_password(target)

    def guess_password(self, target):
        geneSet = "1234567890 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,'()/?"
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return self.get_fitness(genes, target)

        def fnDisplay(genes):
            self.display(genes, target, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(best, target)

    def get_fitness(self,genes, target):
        return sum(1 for expected, actual in zip(target, genes)
                    if expected == actual)

    def display(self, genes, target, startTime):
        timeDiff = datetime.datetime.now() - startTime
        fitness = self.get_fitness(genes, target)
        print( "{}\t{}\t{}\t".format(genes,fitness, timeDiff, ) )


if __name__ == '__main__':
    unittest.main()
