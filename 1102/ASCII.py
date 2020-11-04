print(chr(97)) #a
print(ord("a")) #97

for i in range(ord("a"), ord("z")):
    print(i, end=" ")
print()
for i in range(97, 123):
    print(chr(i), end=" ")
    
print()
for i in range(97, 123):
    print(chr(i+200), end=" ")
    
for i in range(ord("ĩ"), ord("ł")):
    print(chr(i-200), end=" ")
print()
