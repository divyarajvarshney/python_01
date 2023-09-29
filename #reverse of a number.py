#reverse of a number


a=int(input())
rem=1
quo=1
while quo!=0:
    rem=a%10
    print(rem,end="")
    quo=a//10
    a=quo
    

