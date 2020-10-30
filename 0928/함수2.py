def check_pwd():
    pwd = '1234'
    while True:
        answer = input("비밀번호 4자리를 입력하세요")
        if(answer != pwd):
            print("비밀번호가 틀렸습니다 다시 시도합니다.")
        else:
            print("정확한 비밀번호입니다.")
            return

check_pwd()
