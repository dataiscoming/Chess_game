# Pawn object
class Pawn():
    # attributes : initial position (x and y), colour, direction
    def __init__(self,x,y,colour,direction):
        self.x = x
        self.y = y 
        self.colour = colour
        self.direction = direction
        
    #Method Move_to :  the Pawn is able to move of one step in front of him, except it has a enemy on his sides
    def move_to(self,x,y):
        new_position = []
        new_position.append(x+1)
        new_position.append(y+1)
        return new_position  