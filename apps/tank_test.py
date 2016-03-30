import unittest

from tank import Tank

# наследуемся
class TestTankLogic(unittest.TestCase):

    def test_moving(self):

        tank1 = Tank()
        tank2 = Tank()

        self.assertEqual(tank1.pos, 0)
        self.assertEqual(tank2.pos, 0)

        tank1.pos = 100

        self.assertEqual(tank1.pos, 100)
        self.assertEqual(tank2.pos, 0)

    def test_fire(self):
        pass


if __name__ == '__main__':

    # запускает систему тестирования
    unittest.main()
