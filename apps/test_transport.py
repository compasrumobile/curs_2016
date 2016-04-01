import unittest

from transport import Transport

class TestTransport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def setUp(self):
        #print('setUp')
        self.transport = Transport(speed=120)

    def tearDown(self):
        #print('tearDown')
        del self.transport

    def test_drive(self):

        # assert True, True

        self.transport.drive(10)

        self.assertEqual(self.transport.pos, 1200)

    def test_drive2(self):
        self.transport.drive(10)

        self.assertEqual(self.transport.pos, 1200)

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


class TestTransport3(unittest.TestCase):


    def run(self, result=None):
        pass


class TestTransport2(unittest.TestCase):

    def setUp(self):
        self.transport = Transport(speed=120)

    def test_drive(self):
        self.transport.drive(10)

        self.assertEqual(self.transport.pos, 1200)


if __name__=='__main__':
    unittest.main()




