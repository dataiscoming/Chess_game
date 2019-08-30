def ShowBoard(board):
    print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
    for i in range(0,8):
        print("-"*32)
        print(chr(i+97),end="|")
        for j in range(0,8):
            item = board.get((i,j)," ")
            print(str(item)+' |', end = " ")
        print()
    print("-"*32)