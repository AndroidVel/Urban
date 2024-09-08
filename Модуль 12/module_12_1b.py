import unittest
import module_12_1a


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj1 = module_12_1a.Runner('Bob')
        for _ in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 50)

    def test_run(self):
        obj2 = module_12_1a.Runner('Bob')
        for _ in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    def test_chalenge(self):
        obj_1 = module_12_1a.Runner('Bob')
        obj_2 = module_12_1a.Runner('Mark')
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)
