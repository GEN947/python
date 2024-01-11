todos=[]
# 할일 : 할일번호, 할일, 완료
todos.append({'tno':1, 'title':'자바공부', 'finish':False})
todos.append({'tno':2, 'title':'스프링 공부', 'finish':False})
todos.append({'tno':3, 'title':'파이썬 공부', 'finish':False})
tno = 4

def print_list():
    for todo in todos:
        print(todo, end = " ")

def add_todo():
    global tno # 함수 안에서 함수 밖에 있는 변수를 사용하려면 사용한다고 적어준다
    title = input("할일 입력: ")
    todos.append({'tno': tno, 'title': title, 'finish': False})
    tno += 1

def toggle_finish():
    pass

def delete_todo():
    pass

while True:
    print('### 할일 관리 ###')
    print('1. 할일 목록, 2. 할일 추가, 3. 할일 변경, 4. 할일 삭제, 5. finish 변경, 999. 종료')
    select = input('메뉴 선택:')
    if select=='1':
        print_list()
    elif select=='2':
        add_todo()
    elif select=='3':
        toggle_finish()
    elif select=='4':
        delete_todo()
    elif select=='999':
        print('이용해주셔서 감사합니다')
        break