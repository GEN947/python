from func001 import sample, is_major, get_fee, how_price

# unit test(단위 테스트)
# 테스트하는 함수는 pytest로 실행이 가능
# 테스트하는 함수를 작성
# 테스트하는 함수는 pytest로 실행이 가능

# pytest 규칙: 파일 이름, 함수 이름 둘 다 "test_"로 시작할것

def test_sample():
    assert sample() == 10     # assert가 확인하는 방법

def test_is_major():
    assert is_major(20) is True 
    assert is_major(18) is True 
    assert is_major(15) is False 

# 나이를 입력받아 입장료를 리턴하는 함수
# 25 ~ 64세면 3000원, 기타는 무료
    
def test_get_fee():
    assert get_fee(27) == 3000
    assert get_fee(17) == 0
    # assert is_adult(27) == True
    # assert is_adult(17) == False

# 입장료는 3000원이다. 10명은 1인당 2400원
# 인원수를 입력받아 요금 출력
    
def test_how_price():
    assert how_price(10) == 24000
    assert how_price(3) == 9000