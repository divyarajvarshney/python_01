import time



m=8989
a=int(input("e"))
while True:
    
    if a==m:
        print("correct password")
        print(a)
        break

    elif a!=m:
        print("wrong,4 chances left")
        a=int(input("e"))
        times=0
        c=4
        while times<3:
            time.sleep(.5)
            
            if m!=a:
                print("wrong")
                print(times)
                a=int(input("e"))

            else:
                print("guess correctly")
                break
            times+=1
        else:
            print("oout of limit")
            break
                    
            

