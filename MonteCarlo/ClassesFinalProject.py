import numpy as np
import pandas as pd
import random
from itertools import combinations

class Die():
    """
    A class to represent a die.
    
    ...
    Attributes
    ----------
    faces : list
        a series of die faces
        
    weights : list
        a series of weights for each die face, defaults to 1
        
    Methods
    -------
    change_weight(face_changed, new_weight):
        Changes the weight of the face corresponding to the user input

    roll(times_to_roll=1):
        The amount of times the user would like to roll an individual die, defaults to 1

    reveal():
        Returns the dataframe for the dice object 
    """
    def __init__(self, faces, weights = 1):
        """
        Constructs all the necessary attributes for the die object
        
        Parameters
        ----------
            faces : list
                a series of die faces
            weights: list
                a series of weights for each die face, default to 1
        """
        self.faces = pd.Series(faces)
        self.weights = weights
        self._df = pd.DataFrame({'faces' : self.faces,
                                  'weights' : self.weights})

    def change_weight(self, face_changed, new_weight):
        """
        Changes the weight of the face corresponding to the user input
        
        Parameters
        ----------
            face_changed : number or string
                the face that the user wants changed
            new_weight : float
                the number that the user wants the weight of the die face changed to
                
        Returns
        -------
        None
        """
        new_weight = float(new_weight)
        if face_changed in self._df['faces'].values:
            for i in range(0, len(self._df.faces)):
                if self._df['faces'][i] == face_changed:
                    self._df['weights'][i] = new_weight
                else:
                    pass
        else:
            print("The face_changed is not in the list of faces")
           
    def roll(self, times_to_roll=1):
        """
        The amount of times the user would like to roll an individual die, defaults to 1
        
        Parameters
        ----------
        times_to_roll : int
            the amount of times the user wants their die to roll
        
        Returns
        -------
        list_of_outcomes : list
            a list of outcomes for the number of rolls
        """
        list_of_outcomes = random.choices(self._df.faces, weights = self._df.weights, cum_weights = None, k = times_to_roll)
        return list_of_outcomes
    
    def reveal(self):
        """
        Reveals the die dataframe containing the faces and weights of each die
        
        Parameters
        ----------
        None
        
        Returns
        -------
        self._df : pandas dataframe
            the die dataframe containing the faces and weights of each die"""
        return self._df
    
class Game():
    """
    A class to represent a game which consists of rolling one or more dice of the same kind one or more times
    
    ...
    Attributes
    ----------
    list_of_dice : list
        a list of die that were instantiated using the Die class
        
    Methods
    -------
    play(roll_times):
        Rolls each die in the dice list the amount of times specified by the user

    show(choice='wide'):
        Shows the user the results of the rolls.
    """
    
    def __init__(self, list_of_dice):
        """
        Constructs all the necessary attributes for the game object
        
        Parameters
        ----------
        list_of_dice : list
            a list of die that were instantiated using the Die class
        """
        self.list_of_dice = list_of_dice
        
    def play(self, roll_times):
        """
        Rolls each die in the dice list the amount of times specified by the user
        
        Parameters
        ----------
        roll_times : int
            the amount of times the user wants their list of die to roll for the game
        """
        roll_outcome = []
        header = []
        for x in range(0,len(self.list_of_dice)):
            roll_outcome.append(self.list_of_dice[x].roll(roll_times))
        for x in range(0,len(self.list_of_dice)):
            header.append("Die " + str(x+1))
        _faces_df = pd.DataFrame(roll_outcome)
        self._faces_df = _faces_df.T
        self._faces_df = self._faces_df.set_axis(header, axis=1)
        self._faces_df.index.name = 'Roll Number'
              
    def show(self, choice='wide'):
        """
        Shows the user the results of the rolls.
        
        Parameters
        ----------
        choice : string
            the user specifies if they would like the dataframe returned to be 'wide' or 'narrow'
            
        Returns
        -------
        self.faces_df : pandas dataframe
            a dataframe with the roll number as the index, each die from the list_of_dice list as a column, and the results of each roll as a value
            
        self.narrow_df : pandas dataframe
            a dataframe with a two column index consisting of the roll number and the die number and a single column showing the faces rolled"""
        if choice == 'wide':
            return self._faces_df
        elif choice == 'narrow':
            self._narrow_df = pd.DataFrame(self._faces_df.stack())
            return self._narrow_df
        if choice != 'wide' or choice != 'narrow':
            raise Exception("You must either input 'wide' or 'narrow'")
    
class Analyzer():
    """
    A class to represent an analyzer which analyzes a game played of dice played
    
    ...
    Attributes
    ----------
    game : object
        an object instantiated from the game class
    self.access : pandas dataframe
        a dataframe showing the results from the game object
        
    Methods
    -------
    jackpot():
        Shows the user how many times a roll resulted in all faces being the same.

    combo():
        Shows the suer how many combination types of faces were rolled and their counts.

    face_counts_per_roll():
        Computes how many times a given face is rolled for each roll of a game.
    """
    
    def __init__(self, game):
        """
        Constructs all the necessary attributes for the analyzer object
        
        Parameters
        ----------
        game : object
            an object instantiated from the game class
        """
        self.game = game
        self.access = self.game.show()
        
    def jackpot(self):
        """
        Shows the user how many times a roll resulted in all faces being the same.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        jackpot print statement : string
            A string telling the user the number of jackpots in their game"""
        self.jackpot = 0
        results = self.access.nunique(axis = 1).eq(1)
        self.jackpot_df = self.access[self.access.nunique(axis = 1).eq(1)]
        for i in range(0, len(results)):
            if results[i] == True:
                self.jackpot += 1
        return print("Here are your number of jackpots: " + str(self.jackpot))

    def combo(self):
        """
        Shows the suer how many combination types of faces were rolled and their counts.
        """
        self.combo_df = self.access.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('n')
    
    def face_counts_per_roll(self):
        """
        Computes how many times a given face is rolled for each roll of a game.
        """
        self.face_count_df = self.access.apply(pd.Series.value_counts, axis=1).fillna(0)
