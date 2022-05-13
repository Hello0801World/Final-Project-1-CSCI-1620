import unittest
from classes import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tv1=Television(0,0)
        self.tv2=Television(5,5)

    def tearDown(self) -> None:
        del self.tv1
        del self.tv2

    def test_init(self):
        self.assertEqual(self.tv1.channel_up(),1)
        self.assertEqual(self.tv2.channel_up(),0)

    #def test_channel_up(self):
        #self.tv1.channel_up()
        #self.assertEqual(self.tv1.channel_up(), 1)




if __name__ == '__main__':
    unittest.main()
