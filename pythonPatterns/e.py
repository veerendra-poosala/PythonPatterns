#printing pattern d



def e():
    for row in range(7):
        for col in range(5):
            c1=(col==0)
            c2=((row==0 or row==3 or row==6)and(col>0))
            if(c1 or c2):
                print("*",end="")
            else:
                print(end="")
        print()

if __name__=="__main__":
    e=e()
