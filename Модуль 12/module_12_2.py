import runner_and_tournament as rt
from unittest import TestCase


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # TournamentTest.all_results = {}
        pass

    def setUp(self):
        self.run_1 = rt.Runner('Усэйн', 10)
        self.run_2 = rt.Runner('Андрей', 9)
        self.run_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # for place, name in TournamentTest.all_results.values():
        #     print(place, name)
        pass

    def test_1(self):
        self.tour = rt.Tournament(90, self.run_1, self.run_3)  # Усэйн и Ник
        TournamentTest.all_results = self.tour.start()
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results) - 1], self.run_3.__str__())
        print(TournamentTest.all_results)

    def test_2(self):
        self.tour = rt.Tournament(90, self.run_2, self.run_3)  # Андрей и Ник
        TournamentTest.all_results = self.tour.start()
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results) - 1], self.run_3.__str__())
        print(TournamentTest.all_results)

    def test_3(self):
        self.tour = rt.Tournament(90, self.run_1, self.run_2, self.run_3)  # Усэйн, Андрей и Ник
        TournamentTest.all_results = self.tour.start()
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results) - 1], self.run_3.__str__())
        print(TournamentTest.all_results)
