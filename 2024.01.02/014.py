# name = input("이름 입력: ")
# nai = input("나이 입력: ")
# print("이름은", name)
# print("이름은 " + name)
# # f-문자열
# print(f"이름은 {name} 나이는 {nai}")

# hobby = input("취미 입력: ")
# print(f"당신의 취미: {hobby}")

'''
함수는 1가지 일만 담당

ex) 

총점과 평균을 계산하는 함수

총점 계산하는 함수
평균 계산하는 함수

어쨌든 코딩은 재사용하는것이 중요하다
변수도 그렇고 함수도 그렇고 다 그러지 않는가?

한 함수에 여러가지 일을 하는 함수가 재사용하기가 쉬운가?
한 함수에 한가지 일을 하는 함수가 재사용하기가 쉬운가?

'''

first_number = int(input("첫번째 숫자 입력: "))
second_number = int(input("두번째 숫자 입력: "))

print(f"두 수의 합: {first_number+second_number}")

# hap = first_number+second_number
# print(f"두 수의 합: {hap}")

'''
Q. 키보드로 입력 받으면 다 str이다. 왜 그럴까?

1. 샘의 답변: 숫자 3을 입력했을 때 컴퓨터가 인식하기에는 정말 어렵다 애초에 0과 1만 인식할 수 있잖는가
              그렇다면 사람에게는 어떤가? 바로 알 수 있지 않는가? 숫자 3이든 19든 5839든 문자 "안녕", "잘가" 등 보자마자 인식할 수 있다
              그러나 컴퓨터에게는 안 된다는 것이다
              즉, 그래서 컴퓨터는 그냥 문자열로 받고 인간에게 "난 인식하는데 힘드니까너가 바꿔서 써라" 하는거다

2. chatgpt의 답변: (내 chatgpt에 다 있음)
                   유연성의 이유...
''' 
# 덧셈 코드 작성
val1 = None
val2 = None

val1 = int(input("첫번째 숫자: "))
val2 = int(input("두번째 숫자: "))
hap = val1 + val2
print(f"합: {hap}")

# val1, val2에 int 말고 hap에다가 거는 경우도 가능하지만 코드가 길 경우 재사용할때 번거로울 것이다...

'''
val1 = None은 초기값을 설정하는데 None으로 한다는것이다 

val1
val1 = None

이 두 작성문의 차이를 알아야한다는것이다. 
(이유 chahtpgt에 있음)
'''

'''
x = None
print(type(x))

'''