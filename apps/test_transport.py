import unittest

from transport import Transport

class TestTransport(unittest.TestCase):

    def setUp(self):
        self.transport = Transport(speed=120)

    def test_drive(self):
        self.transport.drive(10)

        self.assertEqual(self.transport.pos, 1200)

    def test_drive2(self):
        self.transport.drive(10)

        self.assertEqual(self.transport.pos, 1200)


class TestTransport2(unittest.TestCase):

    def setUp(self):
        self.transport = Transport(speed=120)

    def test_drive(self):
        self.transport.drive(10)

        self.assertEqual(self.transport.pos, 1200)


if __name__=='__main__':
    unittest.main()




