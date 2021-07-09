#printing pattern R



def r():
    for row in range(7):
        for col in range(5):
            c1=( col==0 or row==0)
            c2=(col==4 and(row==1 or row==2 or row==5 or row==6))
            c3=(row==3 and(col>0 and col<3))
            c4=(row==4 and col==3)

            if(c1 or c2 or c3 or c4):
                print("*",end="")
            else:
                print(end=" ")
        print()

if __name__=="__main__":
    r=r()
