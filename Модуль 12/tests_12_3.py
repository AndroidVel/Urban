import unittest
import module_12_1a
import runner_and_tournament as rt


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj1 = module_12_1a.Runner('Bob')
        for _ in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj2 = module_12_1a.Runner('Bob')
        for _ in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_chalenge(self):
        obj_1 = module_12_1a.Runner('Bob')
        obj_2 = module_12_1a.Runner('Mark')
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        self.tour = rt.Tournament(90, self.run_1, self.run_3)  # Усэйн и Ник
        TournamentTest.all_results = self.tour.start()
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results) - 1], self.run_3.__str__())
        print(TournamentTest.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        self.tour = rt.Tournament(90, self.run_2, self.run_3)  # Андрей и Ник
        TournamentTest.all_results = self.tour.start()
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results) - 1], self.run_3.__str__())
        print(TournamentTest.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        self.tour = rt.Tournament(90, self.run_1, self.run_2, self.run_3)  # Усэйн, Андрей и Ник
        TournamentTest.all_results = self.tour.start()
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results) - 1], self.run_3.__str__())
        print(TournamentTest.all_results)
