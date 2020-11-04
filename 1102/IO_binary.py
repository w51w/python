inFile, outFile = None, None
instr = ""
inFile = open("./test01.png", "rb")
outFile = open("./test02.png", "wb")

while True:
    instr = inFile.read(1)
    if not instr :
        break
    outFile.write(instr)
    
inFile.close()
outFile.close()
print("image file copied")