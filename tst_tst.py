__author__ = 'andrew'

import unittest


# наследуемся
class TestStringMethods(unittest.TestCase):

    # тест проверки, что строка правда переводится в верхний регистр
    def test_upper(self):
        # проверяет на идентичность
        self.assertEqual(
            'foo'.upper(),  # что проверяем
            'FOO'           # чем должно быть
        )

    # проверяется isupper
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello worldHHH'
        self.assertEqual(s.split(), ['hello', 'world'])

        # проверяем, что действительно нельзя разделить по числу
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':

    # запускает систему тестирования
    unittest.main()

