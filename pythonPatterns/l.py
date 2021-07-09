#printing pattern L



def l():
    for row in range(7):
        for col in range(5):
            if(col==0 or row==6):
                print("*",end=" ")
            else:
                print(end=" ")
        print()

if __name__=="__main__":
    l=l()
