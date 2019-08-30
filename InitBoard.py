# init board
class InitBoard():
    def __init__(self):
        self.board = {}
    
    def game_begin(self):
        
        from Pawn import Pawn
        
        #uniDict = {WHITE : {Pawn : "♙", Rook : "♖", Knight : "♘", Bishop : "♗", King : "♔",
#                    Queen : "♕" }, BLACK : {Pawn : "♟", Rook : "♜", Knight : "♞", 
#                                Bishop : "♝", King : "♚", Queen : "♛" }}
        uniDict = {"white" : {Pawn : "♙"}, "black" : {Pawn : "♟"}}    
        
        #list_pieces = ['R','K','B','K','Q','B','K','R']
        for i in range(0,8):
            #self.board[(i,0)] = list_pieces[i]
            # board(y,x) 
            self.board[(i,1)] = Pawn(x=1,y=i,colour="white",name=uniDict["white"][Pawn],
                       direction=1)
            self.board[(i,6)] = Pawn(x=1,y=i,colour="black",name=uniDict["black"][Pawn],
                       direction=-1)
            #self.board[(i,7)] = list_pieces[i]
        return self.board