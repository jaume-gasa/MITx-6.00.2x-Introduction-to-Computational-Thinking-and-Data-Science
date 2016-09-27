# Using TDD for developing a simple test simulation
import numpy
import random
import pylab
import unittest

class TestSimpleVirus(unnittest.TestCase):
    myMBP = 0
    myCP = 0
    def setUp(self):
        self.maxBirthProb = myMBP
        self.clearProb = myCP

    def test_getMaxbirthProb(self):
        self.assertEquals(self.maxBirthProb,myMBP)

    def test_getClearProb(self):
        self.assertEquals(self.clearProb, myCP)

    def test_doesClear(self):
        
        self.assertTrue()
    def test_reproduce(self):

if __name__ == '__main__':
    unittest.main()
