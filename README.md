# MonteCarlo 
By Theo Thormann 

A Monte Carlo simulator created for a final project for DS5001 

## Description 
This Monte Carlo simulator consists of three separate classes. The Die class, the Game class, and the Analyzer class 

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
This die object is stored in a private dataframe with two columns, the first column contains the face of the dice and the second column stores the weight of the associated die face.  
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
 The “reveal“ method allows the user to view the private dataframe of the Die object

## Game Class 
The Game class is used to instantiate a game class consisting of a list of dice instantiated by the user. Runing the following code will create a new game: 
```
new_game = Game(list_of_dice) 
```
Within the game class, there are two methods: 

## play() 
The play method will “play” a game with the list of specified dice.  
Example: 
```
new_game.play(10) 
```
This will roll each die in the user set list 10 times. The user can specify any integer in the argument of the method.  

## show() 
The “show” method will show the user either a wide or narrow dataframe depending on what argument the user passes into the method.  
Example 1: 
```
new_game.show(‘wide’) 
```
The wide dataframe consists of an index corresponding to the roll number (starting with zero), columns corresponding to a dice roll, and the face values as the values inside the dataframe.  
Example 2: 
```
New_game.show(‘narrow’) 
```
The narrow dataframe consists of a multi-index with the roll number as the first element of the multi-index and the Dice number as the second element of the multi-index. This dataframe is only one column that shows the face value of the dice roll corresponding to a die during that roll. 
