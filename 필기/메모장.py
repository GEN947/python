# 상수는 대문자로 (모든 언어가 그렇다)
# 사용자가 입력받은 값의 타입은 문자열이다 (모든 언어가 그렇다)
# f-문자열의 f는 format이다.
# for 문의 기본 공식은 (for 변수 in 컬렉션:) 이다.
# sequence는 list, tuple이고 / dictinoary와 set은 아니다 #이게 진짜임
# 값을 찾는거는 for if 그 공식 이용
'''
pass        # "아무것도 하지 말고 지나가라"
continue    # 현재 반복을 중단하고 다음 반복으로 이동

비슷하지만 다르다

예제: 2024.01.10 007.py
'''
# 웹, 앱 개발
'''
앱 개발		프레임워크		        언어
		    react native		   자바 스크립트


		    빅데이터 분석		    python, R
		    인공지능


		    웹, 앱			        JAVA
'''

'''
[framework]

    		요청(request)
사용자 ------------------------> 웹서버


사용자 <------------------------ 웹서버
			응답(response)
            
===================================================
    	    		frontend: html css JavaScript
				↗
	framework    
				↘   
                	backend: 
                    

===================================================
[busniess 로직(업무로직)]

처리
===================================================
full stack: 프론트 백 다 한다 ...

'''

'''
[python]

django
flask
fast api

3개 잘하면 굿
'''

'''
react.js
실습 과제
	일단 본다
    .
    .
월요일
	한번 안 보고 만들어봐 (웬만하면 실패할거)
화요일
	강좌 보면서 따라 만들어봐
수요일
	다시 한번 안 보고 만들어봐 (웬만하면 또 실패)
    내 코드 따라서 만들어봐
수요일 반복
'''
'''
파이썬 list, tuple, set
반복
    for
    while
함수
    git
    dictionary

    html, css

3주차 - 오라클
      - flask 웹서버로 할일관리
3~4주차 - crud 작업
      - 조별로 간단 게시판
'''
'''
책

헤드퍼스트 자바
'''
# # # # # 풀었다고 좋아하지 말고 다르게도 풀어보자 # # # # #

# scope: 변수를 사용할 수 있는 범위
# 블록이 스코프를 생성하는 언어: java       ex) if문 안에서 쓴 것과 그 밖에서 쓴 것을 혼용해서 쓰면 에러..? (chatgpt 도와줘요)
# 함수가 스코프를 생성하는 언어: python
'''
java 스타일

첫번째

input_length = int(input("길이 입력: "))
result_length = None

if input_length > 0:
    result_length = input_length/2.54
elif input_length < 0:
    result_length = input_length*2.54
else:
    result_length = 0
print(result_length)

result_length = None 실행문이 없었다면 이 전체 실행문은 맨 아래의 print(result_length) 실행문이 java에서 안 보였을 것이다.
즉, 에러가 났을 것이라는 것이다.

두번째

input_length = int(input("길이 입력: "))

if input_length > 0:
    result_length = input_length/2.54
    print(result_length)
elif input_length < 0:
    result_length = input_length*2.54
    print(result_length)
else:
    result_length = 0
    print(result_length)

print(result_length) 함수를 처음부터 모든 조건문에 다 넣는것이다 이러면 스코프가 블록인 java에게 어거지로 보여주면서 실행하게 하는것이다.

-----------------------------------------------------------------------------------------------------------------------------

python 스타일

input_length = int(input("길이 입력: "))

if input_length > 0:
    result_length = input_length/2.54
elif input_length < 0:
    result_length = input_length*2.54
else:
    result_length = 0
print(result_length)

파이썬 이녀석은 스코프가 넓기 때문에(?) 어떤 조건문에 있든 파이썬에게 result_length가 다 보인다.
즉 처음에 result_length = 0 이라는 실행문을 넣지 않아도 print(result_length)라는 실행문을 if 조건문마다 넣지 않아도 실행이 되는것이다.
'''
# https://sample.bmaster.kro.kr/ -> 파이썬은 아니지만 dictionary의 개념과 같은 것 .. 
