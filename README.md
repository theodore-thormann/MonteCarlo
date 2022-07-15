# MonteCarlo 
By Theo Thormann 

A Monte Carlo simulator created for a final project for DS5001 

## Description 
This Monte Carlo simulator consists of three separate classes. The Die class, the Game class, and the Analyzer class

#Synopsis

## Installing 
Running the following code from the terminal on your machine inside the directory which you downloaded this repo to will install the MonteCarlo package onto your machine: 
```
$pip install –e .
```

## Importing 
To import the classes used for the MonteCarlo simulator into your IDE or text editor use:
```
from ClassesFinalProject import *
```

## Die Class
The Die class is used to instantiate a die object. Running the following code will instantiate a die object with two attributes of faces or weights: 
```
dieExample = Die([1,2,3,4,5,6]) 
```
For this example, the die object will have 6 faces (1,2,3,4,5,6) and the weights of each face will default to one.  
Within the die class there are three methods: 

### change_weight() 
The “change_weight” method allows the user to change the weight of a specific die face.  
Example: 
```
dieExample.change_weight(6,5) 
```
This will change the example die’s weight of the 6 face to 5, making the odds of rolling a 6 higher than the odds of rolling any other face on the dice. 

### roll() 
The “roll” method allows the user to roll one of their instantiated dice.  
Example: 
```
dieExample.roll(10) 
```
This will “roll” the die ten times, creating a list of outcomes for those 10 rolls. 

### reveal() 
 The “reveal“ method allows the user to view the dataframe of the Die object, with one column displaying the face value and another displaying the weight of that associated face value.

## Game Class 
The Game class is used to instantiate a game class consisting of a list of dice instantiated by the user. Here is an example of code that could run a new game using a list of dice instantiated by the user:
```
new_game = Game(list_of_dice) 
```
Within the game class, there are two methods: 

### play() 
The play method will “play” a game with the list of specified dice.  
Example: 
```
new_game.play(10) 
```
This will roll each die in the user set list 10 times. The user can specify any integer in the argument of the method.  

### show() 
The “show” method will show the user either a wide or narrow dataframe depending on what argument the user passes into the method.  
Example 1: 
```
new_game.show(‘wide’) 
```
The wide dataframe consists of an index corresponding to the roll number (starting with zero), columns corresponding to a dice roll, and the face values as the values inside the dataframe.  
Example 2: 
```
new_game.show(‘narrow’) 
```
The narrow dataframe consists of a multi-index with the roll number as the first element of the multi-index and the Dice number as the second element of the multi-index. This dataframe is only one column that shows the face value of the dice roll corresponding to a die during that roll. 

## Analyzer Class 
The Analyzer class is used to analyze a game object after a game has been played. Here is an example of code that would instantiate a new analyzer class using a game the user created: 
```
new_analyzer = Analyzer(game) 
```
Within the analyzer class there are three methods: 

### jackpot() 
The “jackpot” method computes how many times the game resulted in all faces being identical and returns an integer to the user showing this result. 
Example: 
```
new_analyzer.jackpot() 
```
This method also saves a dataframe with all the rolls that met this criteria.  

### combo() 
The “combo” method saves the distinct combinations of faces rolled, along with their counts. 
Example: 
```
new_analyzer.combo() 
```
The combo method saves these combinations to a dataframe, which can be accessed by the user by using “.combo_df” after their analyzer object. 
Example: 
```
new_analyzer.combo_df 
```

### face_counts_per_roll() 
The face_counts_per_roll method computes how many times a given face is rolled in each event. 
Example: 
```
new_analyzer.face_counts_per_roll() 
```
The face_counts_per_roll method saves to a dataframe, which can be accessed by the user using “.face_count_df” after their analyzer object 
Example:
```
new_analyzer.face_count_df 
```
# API Description

## Die Class
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
        
## Die Class Methods
change_weight(face_changed, new_weight):
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
    
roll(self, times_to_roll=1):
    The amount of times the user would like to roll an individual die, defaults to 1
        
    Parameters
    ----------
    times_to_roll : int
        the amount of times the user wants their die to roll
        
    Returns
    -------
    list_of_outcomes : list
        a list of outcomes for the number of rolls
      
reveal():
    Reveals the die dataframe containing the faces and weights of each die
        
    Parameters
    ----------
    None
        
    Returns
    -------
    self._df : pandas dataframe
        the die dataframe containing the faces and weights of each die
