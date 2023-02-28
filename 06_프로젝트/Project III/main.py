import shopping_bag as sb
import customer,sqlite3,os
path = os.path.dirname(__file__)


while True:
    ex_display = input('''
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈    
    1. 기존회원  2. 비회원  3. 종료
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
    ''')
    if ex_display == '1':
        conn = sqlite3.connect(path + '/customer.sqlite')
        cur = conn.cursor()
        tel = input('검색할 회원의 전화번호를 입력하세요 >>> ')
        cur.execute(f"select * from GUEST where tel = '{tel}'")
        search = cur.fetchone()
        if search == None:
            print('해당하는 전화번호가 없습니다.')
        else:
            print(f'''
        이전 구매 목록은 {search[3]} 입니다.
        ''')
            conn.close()
            sb.main_code()
            
    # 회원일 경우 가장 최근에 주문한 내역을 보여주기 위해 사용
    # GUEST 테이블 안에 tel의 데이터에 입력한 값인 'tel'이 있는 튜플을 search에 가져오고 [3]을 통해 보여주려는 최근주문 보여줌. 
    # 이후 바로 해당 값을 가지고 결제화면으로 넘어가게 하려 했으나 실패.
    elif ex_display == '2' :
        display = input('''
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
   1. 비회원 메뉴선택  2. 회원등록 및 관리  3. 종료
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
>>> ''')

        if display == '1':
            sb.main_code()
        elif display == '2':
            customer.Customer()
        elif display == '3':
            break
        else:
            print('잘못 선택하셨습니다.')
    elif ex_display == '3' :
        break
    else:
        print('잘못 선택하셨습니다.')
    # 1을 선택하면 sb의 main_code 2를 선택하면 customer의 Customer 클래스 실행