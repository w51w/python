filein = None
instr = ""
filein = open("./t.txt", "r", encoding="utf-8") #file read
instr = filein.readlines()

print(instr)
for i in instr:
    print(i, end="")

