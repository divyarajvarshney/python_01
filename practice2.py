#factorial part



n=int(input())
counter=1
i=1
while i<n+1:
    counter*=i
    i+=1
print("factorial of",n,"is",counter)
