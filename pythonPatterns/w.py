#printing pattern W



def w():
    for row in range(6):
        for col in range(7):
            c1=(row<5 and(col==0 or col==3 or col==6))
            c2=((col==1 or col==2 or col==4 or col==5) and row==5)

            if(c1 or c2):
                print("*",end="")
            else:
                print(end=" ")
        print()

if __name__=="__main__":
    w=w()
