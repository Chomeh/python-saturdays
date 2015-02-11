import time

previousNumber=2
currentNumber=3
nextNumber=previousNumber+currentNumber

print(currentNumber)

while True:
    previousNumber=currentNumber
    currentNumber=nextNumber
    nextNumber=previousNumber+currentNumber
    print(currentNumber)
    time.sleep(1)