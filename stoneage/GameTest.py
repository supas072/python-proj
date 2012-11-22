'''
Created on Nov 22, 2012

@author: finn
'''
import unittest
from Game import Game
from Player import Player


class Test(unittest.TestCase):


    def setUp(self):
        self.game = Game()

    def testAddingPlayer(self):
        self.assertEqual(self.game.playerCount(), 0, "no player at start")
        
        self.game.addPlayer(Player())
        self.assertEqual(self.game.playerCount(), 1, "one player added")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()