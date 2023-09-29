# finding sum of a number


c=int(input())
a=str(c)

b=list(a)

v=0
d=0
while v<len(a):
    c=int(a[v])
    d+=c
    v+=1
print(d)
