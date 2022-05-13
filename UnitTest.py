import unittest
from classes import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.channel_value=1
        self.volume_value=0
        self.tv = Television(self.channel_value,self.volume_value)


    #def tearDown(self) -> None:
        #pass

    def test_channel_up(self):
        self.tv.channel_up()
        self.assertEqual(self.tv.channel_up(), 3)
        self.tv.channel_up()
        self.assertEqual(self.tv.channel_up(), 1)


    def test_channel_down(self):
        self.channel_value=4
        self.tv=Television(self.channel_value,self.volume_value)
        self.assertEqual(self.tv.channel_down(),3)
        self.tv.channel_down()
        self.assertEqual(self.tv.channel_down(), 1)



    def test_volume_up(self):
        self.tv.volume_up()
        self.assertEqual(self.tv.volume_up(),2)
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume_up(), 5)



    def test_volume_down(self):
        self.volume_value=5
        self.tv = Television(self.channel_value,self.volume_value)
        self.tv.volume_down()
        self.assertEqual(self.tv.volume_down(),3)
        self.tv.volume_down()
        self.tv.volume_down()
        self.tv.volume_down()
        self.tv.volume_down()
        self.assertEqual(self.tv.volume_down(), 0)



if __name__ == '__main__':
    unittest.main()
