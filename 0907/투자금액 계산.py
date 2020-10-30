seed=1000
y=0
while (seed<=2000):
    y+=1
    interest = seed * 0.03
    seed += interest
print(y)
print(seed)