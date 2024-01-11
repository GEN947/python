numbers = [1,3,5,7]

# 숫자를 입력받아 그 숫자가 numbers에 있는지 출력
'''
num = 5

for item in numbers:
    if item == num:
        print(True)
        break
    else:
        print(False)

# 처음에 1을 본다 -> 없다 즉, else로 넘어가 False 출력
# 다음에 3을 본다 -> 없다 즉, else로 넘어가 False 출력
# 다음에 5를 본다 -> 있다 즉, True 출력하고 break 건 다음 for문 그만 실행
# break 걸렸으므로 7을 안 봄

for item in numbers:
    if item != num:
        print(False)

# 이 실행문을 생각해보자..

# 위 else의 조건과 같지 아니한가
'''

num = 7
is_find = False
# 한번만 찾으면 성공, 실패는 numbers의 모든 값에 대해서 못 찾았어야한다
# 성공과 실패의 조건이 다르다 -> if ~ else ~가 아니다.
for item in numbers:
    if item == num:
        print(True)
        is_find = True
        break
if is_find == False:
    print(False)
'''
for item in numbers:
    if item == num:
        is_find = True
    else:
        is_find = False
print(is_find)
'''

'''
if num in numbers:
    print("출력")
else:
    print("f")
'''