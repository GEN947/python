import datetime as d
# 모듈 이름 바꾸기

print(d.datetime.now())
print(d.datetime.now().date())
print(d.datetime.now().date().weekday())
print(d.datetime.now().date().year)
print(d.datetime.now().time())


# d는 module datetime은 클래스 now()는 메소드
# now()란 현재시간 datetime을 리턴한다