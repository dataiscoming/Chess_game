class Game():
    def __init__(self):
        from InitBoard import InitBoard
        self.board = InitBoard().game_begin()   
        self.main()
        
    def main(self):
        from ShowBoard import ShowBoard
        from Input import Input
        
        while True:
            # show the board with the last move
            ShowBoard(self.board)
            print("Enter the selected piece and its future position :")
            
            # Input the position the selected pieces and propose new position
            input_id = True
            while input_id == True:
                x1,y1,x2,y2 = Input()
                if (x1 in range(8) and y1 in range(8) and x2 in range(8) and y2 in range(8)) or x1 == "quit":
                    input_id = False
            
            if x1 == "quit":
                print("You quited the game.")
                break
                        
            # check the selected piece exist
            try:
                selected = self.board[(y1,x1)]
                #target = self.board[(y2,x2)]
            except:
                print("The selected piece does not exist !")
                selected = False
                #target = False
            
            if selected is not False and (y2,x2) in selected.move(x=x1,y=y1,board=self.board):
                # move the piece
                self.board[(y2,x2)] = selected
    
                # delete the last position of the piece
                del self.board[(y1,x1)]
            else :
                print("probleme")
            
            