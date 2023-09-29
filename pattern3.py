s=10
for i in range(1,s+1):
    for j in range(s-i):
        print(" ",end="")
    for j in range(2*i-1):
        if j==0 or j== 2*i-2 or i==s:
            print("*",end="")
        else:
            print(' ',end='')
    print()

    