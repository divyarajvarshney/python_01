#fibonacci series


n=int(input())
i=0
s=0
p=1
print(s)
print(p)
while i<n:
    s+=1
    p+=s
    i+=1
    print(s,end=" ")
    print(p,end=" ")


