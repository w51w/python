from random import randint

money = 30
while True :
    coin = randint(1,2)
    guess = int(input("앞(1) 뒤(2) 결정>>"))
    if(guess == coin):
        money = money + 9
        print(money)
        if(money >= 100):
            print("승리")
            break;
    else :
        money = money - 10
        print(money)
        if(money <= 0):
            print("패배")
            break;