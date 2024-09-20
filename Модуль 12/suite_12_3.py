import unittest
import tests_12_3

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(tests_12_3.TournamentTest))
suite.addTest(unittest.makeSuite(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
