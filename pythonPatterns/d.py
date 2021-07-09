#printing pattern d

#from pythonPatterns.c import c


def d():
    for row in range(7):
        for col in range(5):
            c1=(col==0)
            c2=((row==0 or row==6)and (col>0 and col<3))
            c3=((row==1 or row==5)and col==3)
            c4=((row>1 and row<5) and col==4)
            if(c1 or c2 or c3 or c4):
                print("*",end="")
            else:
                print(end=" ")
        print()

if __name__=="__main__":
    d=d()

