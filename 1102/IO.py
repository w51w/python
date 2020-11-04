#1. input print
#2. read write

#3. input write
#4. read print

#파일 열기
#r , w ,a 추가  ,t 기본 텍스트모드 ,r+ 읽기/쓰기모드 , b 이진처리

#3. input write (저장)
'''
outfile = None;
outfile = open("./t.txt", "w", encoding='utf-8') #file write (지우고 다시쓰기)
while True:
    instr = input("내용 입력:")
    if instr != "":
        outfile.write(instr + "\n")
    else:
        break
outfile.close()
'''
#4. read print (읽기)
'''
infile, outfile = None,None
instr = ""
infile = open("./t.txt", "r", encoding="utf-8") #file read

while True:
    instr = infile.read()
    if instr != "":
        print(instr + "\n")
    else:
        break
'''
#2. read write (복사)
infile, outfile = None,None
instr = ""
infile = open("./t.txt", "r", encoding="utf-8") #file read
outfile = open("./t_copy.txt", "w", encoding='utf-8') #file write

instr = infile.read()
for i in instr:
    outfile.write(i)
infile.close()
#while True:
#    instr = infile.read()
#    if instr != "":
#        outfile.write(instr + "\n")
#    else:
#        break
outfile.close() #쓰기 close()해야 결과가 보여짐