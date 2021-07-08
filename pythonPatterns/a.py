for rows in range(7):
    for col in range(5):
        if ((col == 0 or col == 4) and rows!=0) or ((rows == 0 or rows == 3 ) and (col > 0 and col < 4)):
            print("*",end="")
            
        else:
            print(end=" ")

    print()