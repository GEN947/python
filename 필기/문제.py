# 문제가 안 보이면 적어보자! like 수학

'''
문제들..

초보를 위한 파이썬 300제
코딩도장
'''

'''고급자'''

# 1부터 100까지 코드를 "최대한" 많이 만들어보시오.

'''중급자'''

# 숫자 입력하면 그 숫자보다 작은 최대의 짝수

'''초급자'''

# 숫자 입력하면 가장 가까운 7의 배수

val1=int(input("수 입력: "))
quo1=val1//7
rem1=val1%7
ans1=quo1*7
print(ans1, rem1)

'''
# 숫자 입력하면 가장 가까운 7의 배수 (if 사용시)

val1 = int(input("수 입력: "))
SEVEN = 7
quo1 = val1//SEVEN
rem1 = val1 % SEVEN
ans1 = 0

if rem1 >= 4:
    quo1 +=1
    ans1 = quo1*SEVEN
    print(f"{quo1}의 가장 가까운 7의 배수는 {ans1}입니다.")
else:
    quo1 += 0
    ans1 = quo1*SEVEN
    print(f"{quo1}의 가장 가까운 7의 배수는 {ans1}입니다.")
'''

'''
27//7=3
27&7=6
4*7=28

21//7=3
21&7=0

'''