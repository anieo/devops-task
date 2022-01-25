
import random

n=random.randint(1,10)
print(n)
out=1
for i in range(1,n+1):
    out*=i
print(f"factorial {n} is {out}")
    
