# main
# include path to the folder containing the classes
import sys
print(sys.path)
sys.path.insert(0, 'C:/Users/LOREN/Desktop/chess_game')

# board = dictoinaire
from InitBoard import InitBoard
from ShowBoard import ShowBoard
board=InitBoard().game_begin()
ShowBoard(board)
board[(1,2)]='P'
ShowBoard(board)

#
pos1=input()
pos2=input()
print(pos1)
print(pos2)

board[(int(pos1),int(pos2))]

# test pawns
from Pawn import Pawn
P1 = Pawn(1,2,"black",1)
P1.move_to(1,2)

# game
from Game import Game
Game()