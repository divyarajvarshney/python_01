#guess the number game

import random
m=random.randint(1,100)
print(m)

n=int(input())
while True :
    if n!=m:
        n=int(input("next  "))
        
    else:
        print(n)
        break

    
