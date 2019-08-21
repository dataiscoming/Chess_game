# init board
class InitBoard():
    def __init__(self):
        self.board = {}
    
    def game_begin(self):
        list_pieces = ['R','K','B','K','Q','B','K','R']
        for i in range(0,8):
            self.board[(i,0)] = list_pieces[i]
            self.board[(i,1)] = 'P'
            self.board[(i,6)] = 'P'
            self.board[(i,7)] = list_pieces[i]
        return self.board