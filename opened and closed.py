from math import sqrt
Number = 1000000
x = []

for i in range(1,Number+1):
    x.append(1)
   #print(i)

#print(x)

for i in range(1,Number+1):
    n = 1
    while n*i-1 < Number:
        if x[n*i-1] == 0:
            x[n*i-1] = 1
        elif x[n*i-1] == 1:
            x[n*i-1] = 0
        n = n+1

n = 0
for i in range(1,Number):

     if not x[i-1]:
        n+=1
        print(f"{n},{i},{int(sqrt(i))}")
         
