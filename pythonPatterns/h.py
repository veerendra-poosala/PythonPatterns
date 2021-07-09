#printing pattern H



def h():
    for row in range(7):
        for col in range(5):
            c1=(col==0)
            c2=((row==3)and(col>0))
            c3=(col==4 or row==3)
            if(c1 or c2 or c3):
                print("*",end="")
            else:
                print(end=" ")
        print()

if __name__=="__main__":
    h=h()
