ages = [10,30,45,18,21,8,19,20,28,33]
print('청소년:')
for a in filter(lambda x:x<20, ages):
    print(a , end=" ");
    
print();
print(list(filter(lambda x:x%2!=1 , range(11))))