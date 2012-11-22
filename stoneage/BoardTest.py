#! /usr/bin/env python3

from Board import Board
from BuildingTile import BuildingTile
import unittest
from Player import Player

class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def testBoardInitialization(self):
        self.assertListEqual([4,4,4,5], self.board.numberOfBuildingTilesLeft())

    def testAvailableBuildingTiles(self):
        abt = self.board.availableBuildingTiles()
        self.assertEqual(4, len(abt))
        self.assertIsInstance(abt[0], BuildingTile)
        
    def testPlacePersons(self):
        self.board.addHunters(2)
        self.board.addLumberjacks(2)

        self.assertEqual(4, self.board.personCount())

        self.board.addClayDiggers(1)
        
        self.assertEqual(5, self.board.personCount())
       
        
def main():
##    suite = unittest.TestLoader().loadTestsFromTestCase(BoardTest)
##    unittest.TextTestRunner(verbosity=2).run(suite)

    # alternatively use this for shorter output
    unittest.main()

if __name__ == '__main__':
    main()
