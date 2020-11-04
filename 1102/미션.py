def Encoding(fileName):
    inFile, outFile = None, None
    instr = ""
    try:
        inFile = open(fileName+".txt", "r", encoding="utf-8")
    except FileNotFoundError:
        print("C\:\\Users\\cjc\\Python\\1102 이곳에 파일이 없습니다")
        return
    outFile = open(fileName+"_encode.txt", "w", encoding="utf-8")
    while True:
        instr = inFile.readline().rstrip() #공백 제거
        if instr != "":
            for i in range(0,len(instr),1):
                print(chr(ord(instr[i]) + 200), end="") #문자 -> 아스키 정수 -> +200 ->문자
                outFile.write(chr(ord(instr[i]) + 200))
            print()
            outFile.write("\n")
        else:
            break;
    inFile.close()
    outFile.close()
    return
def Decoding(fileName):
    inFile, outFile = None, None
    instr = ""
    try:
        inFile = open(fileName+"_encode.txt", "r", encoding="utf-8")
    except FileNotFoundError:
        print("C\:\\Users\\cjc\\Python\\1102 이곳에 파일이 없습니다")
        return  
    outFile = open(fileName+"_decode.txt", "w", encoding="utf-8")  
    while True:
        instr = inFile.readline().rstrip() #공백 제거
        if instr != "":
            for i in range(0,len(instr),1):
                print(chr(ord(instr[i]) - 200), end="") #문자 -> 아스키 정수 -> +200 ->문자
                outFile.write(chr(ord(instr[i]) - 200))
            print()
            outFile.write("\n")
        else:
            break;
    inFile.close()
    outFile.close()
    return

#select = input("1. 암호화 2.복호")
#선택 , 처리 후 카피

Flag = True
while Flag:
    select = input("1. 암호화 2.복호 3.종료 ")

    if select == "1" :
        print("암호화")
        fileName = input("입력파일명 입력(확장자 x)")
        Encoding(fileName)
    elif select == "2" :
        print("복호화")
        fileName = input("입력파일명 입력(확장자, _encode 입력 x)")
        Decoding(fileName)
    else:
        break

