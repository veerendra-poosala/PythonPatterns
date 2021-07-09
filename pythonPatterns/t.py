def t():
    for row in range(6):
        for col in range(5):
            if ((row==0 or (col>1 and col <3))):
                print("*",end=(""))
            else:
                print(end=" ")
        print()


if __name__=="__main__":
    t=t()

