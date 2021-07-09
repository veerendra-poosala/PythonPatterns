def b():
    for row in range(7):
        for col in range(5):
            if (col ==0) or (col==4 and(row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col >0 and col<4)):
                print("*",end=(""))
            else:
                print(end=" ")
        print()

#another way of printing B:
'''
for row in range(7):
    for col in range(5):
        if ((col==0 ) ):
            print("*",end=(""))
        elif((row==0 or row==3 or row==6) and (col > 0 and col < 3)):
            print("*",end=(""))
        
        elif(row ==0 and col==4):
            print("",end=(""))
        elif(row ==3 and col==4):
            print("",end=(""))
        elif(row ==6 and col==4):
            print("",end=(""))

        elif(col==4 and (row!=0 or row!=3 or row!=6)):
            print("*",end="")


        else:
            print(end=" ")
    print()
'''
if __name__=="__main__":
    b=b()