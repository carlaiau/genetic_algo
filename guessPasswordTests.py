import random
import datetime
import genetic
import unittest

class GuessPasswordTests(unittest.TestCase):

    geneset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! "

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return self.get_fitness(genes, target)

        def fnDisplay(candidate):
            self.display(candidate, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)

        self.assertEqual(best.Genes, target)

    def get_fitness(self,genes, target):
        return sum(1 for expected, actual in zip(target, genes)
                    if expected == actual)

    def display(self, candidate, startTime):
        timeDiff = datetime.datetime.now() - startTime
        print( "{}\t{}\t{}\t".format(candidate.Genes, candidate.Fitness, timeDiff))



    def test_Sentence(self):
        self.guess_password("Sentence Here")

    def test_Random(self):
        length = 50
        target = ''.join(random.choice(self.geneset)
                         for _ in range(length))
        self.guess_password(target)


    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)

if __name__ == '__main__':
    unittest.main()

