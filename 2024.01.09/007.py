def 제곱(a):
    print(a*a)
'''
def 제곱(a:int):
    print(a*a)

힌트를 주는거지 제한 하는건 아니다
즉, 힌트는 제대로 줘야된다 int라고 해놨는데 str도 돌아가면 무슨 낭패인가
'''

제곱(10)
제곱(100)

numbers = [1,5,7]
for i in numbers:
    제곱(i)