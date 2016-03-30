import unittest

from tank import Tank

# наследуемся
class TestTankLogic(unittest.TestCase):

    def setUp(self):
        self.tank1 = Tank()
        self.tank2 = Tank()

    def test_moving(self):
        self.assertEqual(self.tank1.pos, 0)
        self.assertEqual(self.tank2.pos, 0)

        self.tank1.pos = 100

        self.assertEqual(self.tank1.pos, 100)
        self.assertEqual(self.tank2.pos, 0)


    def test_fire(self):
        self.tank1.pos = 100

        self.tank2.fire(self.tank1)

        self.assertEqual(self.tank1.pos, 0)


# if __name__ == '__main__':
#
#     # запускает систему тестирования
#     unittest.main()
