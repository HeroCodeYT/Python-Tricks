import time
x= [("1","/","-","\\")for i in range(7)]
for n in x:
    for i in n:
        print(i,end="\r")
        time.sleep(0.3)