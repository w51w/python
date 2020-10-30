min =int(input('min :'))
day = min //(60*24)
re = min % (60*24)
hour = re//60 
min = re % 60
print(day , 'day', hour,'h', min,'m')