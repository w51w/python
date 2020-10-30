
word = "python"
#012345
#-6-5-4-3-2-1
print(word[0:2])  #py
print(word[:2])   #py
print(word[4:])   #on
print(word[:2]+word[2:]) #python
#word[0] = "P" # P로 바꿀 수 없다.
word2="J" + word[1:]
print(word2) #Jython

print(len(word))
'''
a =-1
for i in range(6):
    print(word[a], end='')
    a=a-1
'''
for j in range(-1, -len(word)-1, -1):
    print(word[j], end="")