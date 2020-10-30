d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
   {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
   {'name':'Princess', 'phone':'555-3141', 'email':''},
   {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}
    ]
#전화번호가 8로 끝나는 사용자 이름을 출력하시오
for x in d:
    if(x['phone'][7] == '8'):
        print(x['name'])
#이메일이 없는 사용자 출력
for x in d:
    if(x['email'] == ''):
        print(x['name'])
        print(x['name'] + "는 이메일이 없습니다.")
#사용자 이름을 입력하면 전화번호 이메일 출력
input_name = input('사용자 이름 입력 >>')
for x in d:
    if(x['name'] == input_name):
        print(x['phone']);
        print(x['email']);