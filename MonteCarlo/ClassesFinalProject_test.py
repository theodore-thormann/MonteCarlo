import unittest
from ClassesFinalProject import *
import pandas as pd

class ClassesFinalProjectSuite(unittest.TestCase):
    
    def test_01_change_weight(self):
        """
        Tests the change_weight method by making sure the value from the weight database column is the same as the user input
        """
        test1 = Die([1,2,3])
        test1.change_weight(1,2)
        self.assertEqual(test1._df.faces[1],2)

    def test_02_change_weight(self):
        """
        Tests the change_weight method by returning false saying the weight database column is not equal to the incorrect number
        """
        test2 = Die([1,2,3])
        test2.change_weight(1,2)
        self.assertFalse(test2._df.faces[1] == 3)
        
    def test_03_roll(self):
        """
        Tests the roll method by making sure that it rolls the amount of time the user specifies
        """
        test3 = Die([1,2,3])
        self.assertEqual(len(test3.roll(10)),10)
    
    def test_04_reveal(self):
        """
        Tests the reveal method by making sure the dataframe created equals the number of faces input by the user
        """
        test4 = Die([1,2,3])
        self.assertEqual(len(test4._df), 3)
        
    def test_05_play(self):
        """
        Tests the play method by making sure the length of the resulting play data fram equals the number of plays input by the user
        """
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        game_dice = [die1, die2, die3]
        test5_game = Game(game_dice)
        test5_game.play(10)
        self.assertEqual(len(test5_game._faces_df),10)

    def test_06_show_wide(self):
        """
        Tests the show method to make sure the outputting dataframe is wide by measing the length of columns in the dataframe
        """
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        game_dice = [die1, die2, die3]
        test6_game = Game(game_dice)
        test6_game.play(10)
        test6_game.show('wide')
        self.assertEqual(len(test6_game._faces_df.columns), 3)

    def test_07_show_narrow(self):
        """
        Tests the show method to make sure the outputting dataframe is narrow by measuring the length of the columns in the dataframe
        """
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        game_dice = [die1, die2, die3]
        test7_game = Game(game_dice)
        test7_game.play(10)
        test7_game.show('narrow')
        self.assertEqual(len(test7_game._narrow_df.columns), 1)

    def test_08_jackpot(self):
        """
        Tests the jackpot method by making sure the number of jackpots returned for a very unfair couple of dice is at least 1
        """
        die1 = Die([1,2], [100, 1])
        die2 = Die([1,2], [100, 1])
        game_dice = [die1, die2]
        test8_game = Game(game_dice)
        test8_game.play(10)
        test8_analysis = Analyzer(test8_game)
        test8_analysis.jackpot()
        self.assertTrue(test8_analysis.jackpot > 1)

    def test_09_combos(self):
        """
        Tests the combo method by making sure the dataframe outputs an entry
        """
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        game_dice = [die1, die2, die3]
        test9_game = Game(game_dice)
        test9_game.play(1)
        test9_analysis = Analyzer(test9_game)
        test9_analysis.combo()
        self.assertEqual(len(test9_analysis.combo_df), 1)

    def test_10_face_counts_per_roll(self):
        """
        Tests the face_counts_per_roll method by rolling a dice only one time and making sure the result sums to 1
        """
        die1 = Die([1,2,3,4,5,6])
        game_dice = [die1]
        test10_game = Game(game_dice)
        test10_game.play(1)
        test10_analysis = Analyzer(test10_game)
        test10_analysis.face_counts_per_roll()
        self.assertEqual(test10_analysis.face_count_df.sum(axis=1).values, 1)


        
        
if __name__ == '__main__':

    unittest.main(verbosity=3)