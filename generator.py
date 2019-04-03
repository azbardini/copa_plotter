from random import randint
import time

startTime = 0
while True:
    startTime += 1
    print(randint(0,9))
    f = open("example.txt", "a")
    f.write(str(startTime)+','+str(randint(0,9))+"\n")
    f.close
    time.sleep(1)
