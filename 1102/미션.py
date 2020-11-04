#select = input("1. 암호화 2.복호")
#선택 , 처리 후 카피
  

inFile, outFile = None, None
instr = ""

InfileName = input("입력파일명 입력")

inFile = open(InfileName, "r", encoding="utf-8")
while True:
    instr = inFile.readline().rstrip() #공백 제거
    if instr != "":
        print(instr)
        print(ord(str))
    else:
        break;

inFile.close()