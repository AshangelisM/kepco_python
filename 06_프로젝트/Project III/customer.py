import re
import sqlite3,os,shopping_bag

path = os.path.dirname(__file__)


# 고객관리 클래스 생성

class Customer:

    # 직접적으로 사용하진 않으나 테이블의 전체 고객정보를 조회하고 출력하는 함수를 설정.

    def all_customer(self):
        conn = sqlite3.connect(path + '/customer.sqlite')
        cur = conn.cursor()
        sql = 'select * from '
        cur.execute(sql)
        for item in cur.fetchall():
            print(item)
        conn.close()

    # 앞서 생성한 전체 고객정보를 기본값으로 설정, 선언.

    def __init__(self):
        self.all_customer
        while True:
            self.exe(self.choice())
    
    # 회원정보 메뉴를 출력하고 세부메뉴로 진입하는 함수

    def choice(self):
        choice = input('''
------------------------------------------------------
1.회원가입 2.회원검색 3.회원정보수정 4.회원정보삭제 5.종료
>>> ''')
        return choice
    def exe(self,choice):
        if choice == '1':
            self.insert_customer()
        elif choice == '2':
            self.search_customer()
        elif choice == '3':
            self.update_customer()
        elif choice == '4':
            self.delete_customer()
        elif choice == '5':
            print('종료합니다.')
            return shopping_bag.main_code() #종료할경우 shopping_bag의 main_code 실행하도록 만듦.
        else:
            print('잘못선택하셨습니다.')


    # sqlite를 이용하여 전화번호와 성명을 기입함으로써 가입이 가능하게 함.
    # 다만 세번째 열인 포인트에는 0, 네번째 열인 직전주문목록은 공란으로 입력되게끔 함.

    def insert_customer(self):
        conn = sqlite3.connect(path + '/customer.sqlite')
        cur = conn.cursor()
        while True:
            tel = input('전화번호를 입력하세요 >>> ')
            sql = 'select * from GUEST'
            cur.execute(sql)
            result = cur.fetchall() #guest에 저장된 값을 튜플로 가져옴.
            check = None
            for idx,i in enumerate(result):
                if i[0] == tel:      #튜플이므로 'tel'에 해당하는 값을 가져오기위해 i[0]사용
                    check = idx
                    break
            if check == None:
                p = re.compile('[0-9]{3}-[0-9]{4}-[0-9]{4}') #전화번호는 중복되지 않는 값이어야 하고 형식을 맞춰야 함.
                if p.search(tel) != None:
                    break
                else:
                    print('000-0000-0000형식을 지켜서 입력하세요.') #형식을 지키지 않을 경우 형식을 지키라고 알려줌.
            else:
                print('중복되는 전화번호가 있습니다.')
        name = input('성명을 입력하세요 >>> ')
        sql = 'insert into GUEST values(?,?,?,?)'
        cur.execute(sql,(tel, name, 0, ''))
        conn.commit()
        conn.close()


    # sqlite와 파이썬 연계에 있어 쟁점이 되었던 부분.
    # where 조건문에 입력값을 대조하여 일치하는 당해 회원정보만을 출력하는 구조.

    def search_customer(self):
        conn = sqlite3.connect(path + '/customer.sqlite')
        cur = conn.cursor()
        tel = input('검색할 회원의 전화번호를 입력하세요 >>> ')
        cur.execute(f"select * from GUEST where tel = '{tel}'")
        search = cur.fetchone()   # GUEST테이블에서 tel의 데이터가 입력한 'tel'과 같으면 search에 가져옴.
                                  # (전화번호는 중복되지 않으므로 전화번호를 통해 가져올 수 있는 데이터는 하나!)
        while True:
            if search == None:
                print('해당하는 전화번호가 없습니다.')
                break
            else:
                print(f'''
        전화번호 : {search[0]}
        성명 : {search[1]}
        포인트 : {search[2]}
        이전구매목록 : {search[3]}
        ''')
                break
            # search값이 None일 경우 입력한 값이 tel의 데이터에 없다는 것이므로 해당하는 번호가 없다고 보여줌.
            # 그게 아닐 경우 저장된 정보를 보여줌.
        conn.close()


    # update-set 쿼리를 활용하여 DB상의 회원정보를 수정하는 기능.
    # 다만 포인트나 직전주문내역을 수정할 수 있어서는 아니되므로, 전화번호와 성명만 수정 가능.
 
    def update_customer(self):
        conn = sqlite3.connect(path + '/customer.sqlite')
        cur = conn.cursor()
        tel = input('수정할 회원의 전화번호를 입력하세요 >>> ')
        check = 1
        while check:
            col = input('수정할 항목을 입력하세요 (tel, name) >>> ')
            if col in ('tel','name','',''):
                check = 0
        value = input(f'{col} 항목의 수정할 내용을 입력하세요 >>> ')
        sql = f'update GUEST set {col} = ? where tel = ? '
        cur.execute(sql,(value,tel))
        conn.commit()
        conn.close()
    # tel을 통해 번호를 받고 col을 통해 수정할 수 있는 값인 tel,name을 받음.
    # tel의 경우 중복되지 않아야 하고 일정 형식을 받아야 하나 구현에 실패.


    # delete from 쿼리를 활용하여 특정 회원정보를 삭제하는 함수.

    def delete_customer(self):
        conn = sqlite3.connect(path + '/customer.sqlite')
        cur = conn.cursor()
        tel = input('삭제할 회원의 전화번호를 입력하세요 >>> ')
        sql = 'delete from GUEST where tel = ?'
        cur.execute(sql,[tel])
        conn.commit()
        conn.close()


