#printing pattern O



def o():
    for row in range(7):
        for col in range(5):
            c1=((row>0 and row <6) and (col==0 or col==4))
            c2=((row==0 or row==6 ) and (col>0 and col<4))
            if(c1 or c2):
                print("*",end="")
            else:
                print(end=" ")
        print()

if __name__=="__main__":
    o=o()
