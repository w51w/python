
#1. read() 파일 전체를 읽을 수 있다
#2. read(n) n개의 문자를 읽을 수 있다
#3. readlines()전체 파일을 읽고자 할 때 , 파일의 각 줄을 읽어 리스트에 저장, 한줄이 리스트의 한 항목이 된다 ,  항복의 끝에는 줄바꿈'\n'이 있다
#4. readline() 파일에 한줄씩 읽고자 할 때 사용

filein = None
filein = open("./t.txt", "r", encoding="utf-8") #file read
#readall = filein.read()
#readall = filein.read(7)
#readall = filein.readlines()
i=1
while True:

    readall = filein.readline().rstrip() #공백 제거
    if readall != "":
        print("%d. %s" %(i, readall))
        i = i+1
    else:
        break;
filein.close()
