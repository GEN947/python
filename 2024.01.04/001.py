# 75, 80, 70이라는 국어 점수가 있다 -> 집합 타입(sequence)

first_kor_score = 75
second_kor_score = 80
third_kor_score = 70

# 값 하나를 저장: int, float, str, bool
# 값 여러개를 저장: list, tuple

kor = [75,80,70] # [0번째, 1번째, 2번째,... ]
# kor의 타입 출력
print(type(kor))
print(kor[0])
print(kor[1])
print(kor[2])

# 조건문, 반복문
for item in kor:  # kor 리스트의 원소를 하나씩 꺼내서 item에 담는다
    print(item)

# 리스트를 쓰는 이유는 변수의 개수를 줄일 수 있다 -> 다루기가 쉽다 -> "쉬운 코드가 되는거다"

# 리스트는 변경 가능하고, 튜플은 변경 불가능
리스트 = ["사과", "귤", "수박"]
튜플 = ("사과", "귤", "수박")
# CRUD - Create Read Update Delete / Create, Update, Delete - 변경에 해당

for aaa in 튜플:
    print(aaa)

for bbb in 리스트:
    print(bbb)