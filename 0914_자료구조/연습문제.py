#str = input("문자를입력하세요")
str = 'I love Python'
word = "love"
print(len(str))
'''
for i in range(0,10,1):
    print(word, end="")
print("");
'''
print(word * 10) #2
print(str[0])
print(str[:3])
print(str[len(str)-3:])
for j in range(-1, -len(str)-1, -1):
    print(str[j], end="")
print("")
if(str[6].isalpha()): #7
    print(str[6])
else:
    print("문자가 없습니다")
print(word[1:len(word)-1]) #8번 -2가 더 깔끔
print(str.upper())
print(str.lower())
print(str.replace('o', 'e'))
