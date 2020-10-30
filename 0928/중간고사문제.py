scores=[]
sum=0
for i in range(5):
    value = int (input ('성적입력 '))
    scores.append(value)
    sum+=value

avg=sum/len(scores)
highScore=0
for i in range(len(scores)) :
    if scores[i] >= 80 :
        highScore += 1
print('성적평균은 ',avg,'입니다')
print('80점 이상은 ',highScore,'명입니다')

print(scores)
