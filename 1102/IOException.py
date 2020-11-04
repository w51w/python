infile = None;
instr =""
fname = input("파일명을 입력하세요")

try:
    infile = open(fname, "r", encoding="utf-8")
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
else:
    instr = infile.readlines()
    for i in range(len(instr)):
        print(i+1,". ", instr[i], sep="")
    infile.close()