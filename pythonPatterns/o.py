#Here i just want to print pattern o

n=int(input("Enter no.of rows :"))
for i in range(n):# i for colomns
    for k in range(n-i):
        print("*",end=" ")
    for j in range(0,i,1):
        print(j,end=" ")
    #print(end="")
    for l in range((n-1)-i,-1,-1):
        print(l,end=" ")
    
    print()
    #print(end="")
    