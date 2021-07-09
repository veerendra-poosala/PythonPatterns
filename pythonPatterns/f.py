#printing pattern f



def f():
    for row in range(7):
        for col in range(5):
            c1=(col==0)
            c2=((row==0 or row==3)and(col>0))
            if(c1 or c2):
                print("*",end="")
            else:
                print(end="")
        print()

if __name__=="__main__":
    f=f()
