import imp
from time import sleep
for x in range(1,11):
    for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
        sleep(0.1)
        if x == 10:
            print('(Done ;)' , end='')
            break
        else:
            print('Loading ' +i, end = '\r')