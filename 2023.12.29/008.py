# 함수, 변수 -> 이름을 가진다 -> 재사용하려고 / 재사용 가능하면 생산성이 높아진다

# 이름은 간결한것만이 좋은게 아니고 최대한 길게, 가독성 좋게 쓰는 것이 좋다 -> 최대한 길게는 이름을 보자마자 무슨 뜻인지 알게끔
# 이름은 알아보기 쉽게, 소문자와 _로 만든다

SumOfAllScores=220 # C 특
sumOfAllScores=220 # java 특
sum_of_all_scores=220 # python 특

# 키워드(예약어)는 사용할 수 없다
# 파이썬이 사용하는 단어

name_of_jo = "조정빈"
age_of_jo = 21

print("제 이름은", name_of_jo)

age_of_jo = age_of_jo + 1
print("나이는", age_of_jo, "살")

my_dog_name = "초코"

print("우리집 강아지 이름은", my_dog_name, "에요")
print(my_dog_name, "는 산책을 아주 좋아해요")

print("우리집 강아지 이름은 " + my_dog_name + "에요")
print(my_dog_name + "는 산책을 아주 좋아해요")

salary = 3000000
print("급여: " + str(salary))
print("급여:", salary)

samsung_electronics_stock_price = 78500
print("총 평가금액: " + str(samsung_electronics_stock_price*10) + "원")

고객의주가총액=samsung_electronics_stock_price*10
print("총 평가금액: " + str(고객의주가총액) + "원")