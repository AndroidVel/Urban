import logging
import unittest
import rt_with_exceptions


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            obj1 = rt_with_exceptions.Runner('Bob', -7)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                obj1.walk()
            self.assertEqual(obj1.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            obj2 = rt_with_exceptions.Runner(123)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                obj2.run()
            self.assertEqual(obj2.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_chalenge(self):
        obj_1 = rt_with_exceptions.Runner('Bob')
        obj_2 = rt_with_exceptions.Runner('Mark')
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)
