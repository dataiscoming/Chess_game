def Input():
    import string
    try:
        in1=input()
        in2=input()
        
        possible_input=[]
        for i in ['a','b','c','d','e','f','g','h']:
            for j in range(8):
                possible_input.append(i+str(j+1))
        possible_input.append("quit")
        possible_input.append("")
        
        if in1.lower() != "quit" and in2.lower() != "quit":
            if in1 in possible_input and in2 in possible_input:
                y1 = int(ord(in1[0].lower()) - 97)  
                x1 = int(in1[1])-1
                y2 = int(ord(in2[0].lower()) - 97)
                x2 = int(in2[1])-1
                return x1,y1,x2,y2
            else :
                print("position selected are out of bounds !")
                return -1,-1,-1,-1
        else :
            return "quit","quit","quit","quit"    
        
    except:
        print("Error in the input !")