# init board
class InitBoard():
    def __init__(self):
        self.board = {}
    
    def game_begin(self):
        
        from Pieces import Pieces
        
        uniDict = {"white" : {"Pawn" : "♙","Rook" : "♖", "Knight" : "♘", "Bishop" : "♗",
                              "King" : "♔", "Queen" : "♕" }, 
                   "black" : {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝",
                              "King" : "♚", "Queen" : "♛"}}    
        
        pieces_list=["Rook","Knight","Bishop","Queen","King","Bishop","Knight","Rook"] 
    
        for i in range(0,8):
            # board(y,x) 
            self.board[(i,0)] = Pieces(x=0,y=i,colour="white",
                       name=uniDict["white"][pieces_list[i]],direction=1, 
                       category= pieces_list[i])
            self.board[(i,1)] = Pieces(x=1,y=i,colour="white",name=uniDict["white"]["Pawn"],
                       direction=1, category= "Pawn")
            self.board[(i,6)] = Pieces(x=1,y=i,colour="black",name=uniDict["black"]["Pawn"],
                       direction=-1, category= "Pawn")
            self.board[(i,7)] = Pieces(x=7,y=i,colour="black",
                       name=uniDict["black"][pieces_list[i]],direction=1, 
                       category= pieces_list[i])
        return self.board