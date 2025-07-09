from math import sqrt
import time

def count_divisors(n):
    count = 0
    root = int(sqrt(n))
    for i in range(1, root + 1):
        if n % i == 0:
            count += 2 if i * i != n else 1  # Count both divisors
    return count

t = time.time()
i = 1

while True:
    # Use direct formula for nth triangular number
    A = i * (i + 1) // 2  
    divisors = count_divisors(A)

    if divisors >= 300:
        print(f'{A}, {divisors}')
        
    
    i += 1

print(f'Time: {time.time() - t} s')
