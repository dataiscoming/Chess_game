# Pawn object
class Pawn():
    # attributes : initial position (x and y), colour,name, direction
    def __init__(self,x,y,colour,name,direction):
        self.x = x
        self.y = y 
        self.colour = colour
        self.direction = direction
        self.name = name
        
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
        
    #Method Move_to: avalaible move 
    def move(self,x,y,board):
        new_position = []
        new_position.append((y,x+self.direction))
        
        try:
            if board[(y+1,x+self.direction)].colour != self.colour : 
                new_position.append((y+1,x+self.direction))
        except:
            new_position.append((y,x+self.direction))
        
        try:
            if board[(y-1,x+self.direction)].colour != self.colour :
                new_position.append((y-1,x+self.direction))
        except:
            new_position.append((y,x+self.direction))
        return new_position  