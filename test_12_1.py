from unittest import TestCase
from module_12_1 import Runner


class RunnerTest(TestCase):

    def test_walk(self):
        runner = Runner('Имя')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)

    def test_run(self):
        runner = Runner('Имя')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner('Имя')
        runner2 = Runner('Имя')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


