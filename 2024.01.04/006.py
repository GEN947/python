# module: 남의 코드를 가져와 기능 확장 (vscode의 확장 프로그램 비슷한거)
# library: 기능들 (개발자들이 선택해서 사용 가능), framework: 기능들 + 사용법 (사용법이 정해져있음)

import random

random.random()  # 앞에 있는 random은 모듈의 이름 / 뒤에 있는 random은 함수의 이름
'''
# 1보다 작은 실수
a = random.random()

# 10보다 작은 실수
b = random.random()*10
'''

for i in range(5):  # 파이썬의 for문은 리스트만큼 반복한다
    b = int(random.random()*10)
    print(b)

print(int(random.random()*10))

c = int(random.random()*11)  # random.random()은 0.00~, 0.99~ 이런식으로 나오기 때문에 10만 곱하면 0~9까지만 나온다.

d = int((random.random()*10)+1)
print(d)
