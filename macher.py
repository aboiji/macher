import random

# 남자이름, 여자이름 
boyname = ["남자1", "남자2", "남자3", "남자4", "남자5"]
girlname = ["여자1", "여자2", "여자3", "여자4", "여자5"]


# 남자와 여자 조아하는 순서를 렌덤으로
boylike = dict()
girllike = dict()
for boy in boyname:
    temp = girlname.copy()
    random.shuffle(temp)
    boylike[boy] = temp.copy()
for girl in girlname:
    temp = boyname.copy()
    random.shuffle(temp)
    girllike[girl] = temp.copy()


singleboy = boyname.copy()  # 아직 커플이 아닌 남자아이
boycount = dict()           # 남자아이 각각 제안해본 횟수
for boy in boyname:
    boycount[boy] = 0       # 다들 해본적 없으므로 0

couple = dict()             # 커플

while singleboy:            # 혼자인 남자가 남지 않을때까지 반복
    boy = singleboy.pop(0)
    girl = boylike[boy][boycount[boy]]
    boycount[boy] += 1

    if girl in couple:                                # 이미 커플일떄
        boyfriend = couple[girl]
        if girllike[girl].index(boyfriend) < girllike[girl].index(boy):      # 지금 약혼자와의 선호도 비교
            singleboy.append(boyfriend)
            couple[girl] = boy
        else:
            singleboy.append(boy)
    
    else:
        couple[girl] = boy


print("남자 선호도")
for boy in boyname:
    print(boy, boylike[boy])

print("여자 선호도")
for girl in girlname:
    print( girl, girllike[girl])

print("결과 ")
for girl, boy in couple.items():
    print(girl, boy)  
    

