#   armstrong of a number


d=int(input("enter "))
k=str(d)
a=list(k)

m=0
c=0

while m<len(a):
    v=int(a[m])
    z=v**3
    c+=z
    m+=1
print(c)
    
 

if c==d:
    print(True)
else:
    print("false")
    

