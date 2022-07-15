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
__init__(faces, weights = 1):
    Constructs all the necessary attributes for the die object
        
    Parameters
    ----------
        faces : list
            a series of die faces
        weights: list
            a series of weights for each die face, default to 1
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
    
roll(times_to_roll=1):
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
        
## Game Class
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
## Game Class Methods
__init__(list_of_dice):
    Constructs all the necessary attributes for the game object
        
    Parameters
    ----------
    list_of_dice : list
        a list of die that were instantiated using the Die class

play(roll_times):
    Rolls each die in the dice list the amount of times specified by the user
        
    Parameters
    ----------
    roll_times : int
        the amount of times the user wants their list of die to roll for the game
        
show(choice='wide'):
    Shows the user the results of the rolls.
        
    Parameters
    ----------
    choice : string
        the user specifies if they would like the dataframe returned to be 'wide' or 'narrow'
            
    Returns
    -------
    self.faces_df : pandas dataframe
        a dataframe with the roll number as the index, each die from the list_of_dice list as a column and the results of each roll as a value
            
    self.narrow_df : pandas dataframe
        a dataframe with a two column index consisting of the roll number and the die number and a single column showing the faces rolled        
        
## Analyzer Class
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
        
## Analyzer Class Methods
__init__(game):

    Constructs all the necessary attributes for the analyzer object
        
    Parameters
    ----------
    game : object
        an object instantiated from the game class
        
jackpot():

    Shows the user how many times a roll resulted in all faces being the same.
        
    Parameters
    ----------
    None
        
    Returns
    -------
    jackpot print statement : string
        A string telling the user the number of jackpots in their game
        
combo():
    Stores a data frame of how many combination types of faces were rolled and their counts.
    
face_counts_per_roll():
    Computes how many times a given face is rolled for each roll of a game.    
