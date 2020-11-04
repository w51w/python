#with as ___:
#명시적으로 close()를 호출하지 않아도 파일이 항상 닫힘
outfile = None;
with open("./t.txt", "w", encoding='utf-8') as outfile:
    outfile.write("성춘향 010-1234-5678\n")
    outfile.write("이몽룡 010-1111-2222\n")
    outfile.write("변학도 010-3333-4444\n")
    outfile.write("장금이 010-5555-6666\n")
#    outfile.write("홍길동 010-7777-8888\n")
    #outfile.close()