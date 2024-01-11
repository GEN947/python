import e005
from e005 import hello

# e005에 파이썬이라고 출력하는 함수를 정의하고 006.py에서 호출하시오

from e005 import print_python

print_python()

'''
import a

a.b()

이렇게 쓰면 a라는 모듈 전체를 import 하는거다
그래서 a.b()라는 멤버연산자를 써야한다
---------------------------------------
from a import b

b()

이렇게 쓰면 a라는 모듈 중에 b라는 함수를 가져오는거다
그래서 b만 써도 된다
----------------------------
import math as m

m.b()

이렇게 쓰면 math라는 모듈을 m이라 쓸 수 있게 하는거다.
math.b()라 써야됐던걸 b라 쓸 수 있다 
'''
# 병렬 프로그램...? 이라 안 돌아간다..?
hello()
print_python()
message()