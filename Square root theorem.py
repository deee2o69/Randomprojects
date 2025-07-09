import math
NUM = 3
Currentsqr = 1
sqrtCurrent = 1
while True:
    Actual_SquareRoot = math.sqrt(NUM)
    
    if not(Actual_SquareRoot % 1.0):
        Currentsqr = NUM
        sqrtCurrent = Actual_SquareRoot
        #print(f'{NUM},{sqrtCurrent}')
    else :   
        D = (NUM-Currentsqr)/(2*sqrtCurrent)
        E = (sqrtCurrent+D)
        F = abs(Actual_SquareRoot-E)
        if (F > 0.1):
            print(f'{NUM:0.3f},{Actual_SquareRoot:0.3f},{E:0.3f},{F:0.3f}')

    NUM = NUM+1

    if not (NUM%1000000000):
        print(f'{NUM/1000000000} e9')

