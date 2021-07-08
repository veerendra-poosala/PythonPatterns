#Here i just want to print pattern o

n=int(input("Enter no.of rows :"))
for i in range(n,0,-1):# i for rows
    for j in range(i,0,-1):#j for coloumns(1-5)
        print("*",end=" ")
    for k in range(2*(n-i)):#k for printing spaces on columns
        print(" ",end=" ")
    for l in range(i,0,-1):
        print("*",end=" ")
    print()

for i in range(1,n):
    for j in range(i+1):
        print("*",end=" ")
    for k in range(2*(n-i-1)):
        print(" ",end=" ")
    for l in range(i+1):
        print("*",end=" ")
    print()