import myfood
    
foodlist = ["짜장면","짬뽕","탕수육","우동","돈까스"]
myfood.print_list(foodlist)
for i ,food in enumerate (foodlist):
    print(f"{i+1}.{food}")
#리스트중에 먹고 싶은 메뉴가 없으면
#사용자가 입력을 한다
#만약에 그만을 입력하면 입력이 끝나고
# 음식 리스트 출력하고 추천 메뉴가 출력
while True :
#우리가 추가해서 그중에서 추천 했으면 좋겠다
    addfood = input("추가 음식 입력:")
    print(f"당신이 입력한 내용 : {addfood}")
    #만약에 입력한 글자가 그만과 같다면
    #무한반복을 멈춤
    if addfood == "그만":
        break
    foodlist.append(addfood)
#음식 리스트 출력
myfood.print_list(foodlist)
print("당신의 음식 데이터를 ai가 분석해서 5개를 추천합니다.")
myfood.print_rand_list(foodlist)
# 