# main
# include path to the folder containing the classes
import sys
print(sys.path)
sys.path.insert(0, 'C:/Users/quent/Documents/projects/Chess_game')
   
# Start the game
from Game import Game
Game()