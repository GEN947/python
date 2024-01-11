# 할일 관리
todos = [
    {"tno": 1, "title": "할일 1", "reg_day": "2024-01-09", "finish": False},
    {"tno": 2, "title": "할일 3", "reg_day": "2024-01-09", "finish": False}
]
tno = 2

# Read: 
for todo in todos:
    print(todo)

# 할일 번호를 입력 받아 찾아서 출력
input_tno = int(input("할일 입력: "))
찾았는가 = False
for tno in todos:
    if input_tno == tno["tno"]:
        print(tno)
        찾았는가 = True
        break
    # else:
    #     print("올바른 값만 입력해주세요")         # print를 옮겨볼 생각을 안 해봄
if 찾았는가 == False:
    print("할일을 찾을 수 없습니다")
