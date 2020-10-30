sum = 0
i = 1
while(i<1001):    
    for s in str(i):
        sum += int(s)
    print(sum)
    i= i+1
print("1~1000 ,마지막 계산 :" + str(sum))
