# main
# include path to the folder containing the classes
import sys
print(sys.path)
sys.path.insert(0, 'C:/Users/quent/Documents/projects/Chess_game')
   
# Start the game
from Game import Game
Game()

#
from Pawn import Pawn

a = Pawn(1,1,colour="black",name="p",direction=1)

a.colour

from InitBoard import InitBoard
board = InitBoard().game_begin()

board[(0,1)].colour != "white"


new_position=[]
try:
    if board[(0,2)].colour != "black":
        new_position.append((4,4))    
except: 
    new_position.append((-1,-1))
    
    #print("aa")