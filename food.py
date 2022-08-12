import random
from traceback import print_tb
foodlist = ["짜장면","짬뽕","탕수육","우동","돈까스"]
food = random.choice(foodlist)
print(food)
#5번을 연속으로 추천해보자
for i in range(5) :
    # print(i+1)
    food = random.choice(foodlist)
    #print(i + 1 + "." + food)
    print(f"{i+1}.{food}")
print("종료")


