# MonteCarlo 
By Theo Thormann 

A Monte Carlo simulator created for a final project for DS5001 

# Description 
This Monte Carlo simulator consists of three separate classes. The Die class, the Game class, and the Analyzer class 

## Installing 
Running the following code from the terminal on your machine inside the directory which you downloaded this repo to will install the MonteCarlo package onto your machine: 
$pip install –e . 

## Importing 
To import the classes used for the MonteCarlo simulator into your IDE or text editor use: 
from ClassesFinalProject import * 

# Die 
The Die class is used to instantiate a die object. Running the following code will instantiate a die object with two attributes of faces or weights: 
dieExample = Die([1,2,3,4,5,6]) 
For this example, the die object will have 6 faces (1,2,3,4,5,6) and the weights of each face will default to one. 
This die object is stored in a private dataframe with two columns, the first column contains the face of the dice and the second column stores the weight of the associated die face.  
Within the die class there are three methods: 

### change_weight() 
The “change_weight” method allows the user to change the weight of a specific die face.  
Example: 
dieExample.change_weight(6,5) 
This will change the example die’s weight of the 6 face to 5, making the odds of rolling a 6 higher than the odds of rolling any other face on the dice. 

###roll() 
The “roll” method allows the user to roll one of their instantiated dice.  
Example: 
dieExample.roll(10) 
This will “roll” the die ten times, creating a list of outcomes for those 10 rolls. 

###reveal() 
 The “reveal“ method allows the user to view the private dataframe of the Die object 
