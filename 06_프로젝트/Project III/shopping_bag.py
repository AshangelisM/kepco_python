import sqlite3,os

path = os.path.dirname(__file__)

# sandwich 메뉴판:딕셔너리(고정값) - 6개 항목의 각각의 특성을 지정함.
sandwich = [{'sname': '이탈리안비엠티', 'bread': '파마산오레가노', 'toasting': 'O',
             'sauce': '랜치&어니언', 'price': '6200'},
            {'sname': '터키', 'bread': '허니오트', 'toasting': 'X',
             'sauce': '올리브오일&소금&후추', 'price': '5400'},
            {'sname': '에그마요', 'bread': '하티', 'toasting': 'X',
             'sauce': '스위트칠리', 'price': '5800'},
            {'sname': '스테이크', 'bread': '플랫', 'toasting': 'O',
             'sauce': '바베큐&마요네즈', 'price': '7200'},
            {'sname': '쉬림프', 'bread': '화이트', 'toasting': 'X',
             'sauce': '핫칠리', 'price': '6300'},
            {'sname': 'BLT', 'bread': '위트', 'toasting': 'O', 
             'sauce': '랜치&스위트칠리', 'price': '6000'}]

# 수정시 정해진 값으로만 수정하기 위해 리스트를 생성.
bread = ['파마산오레가노','허니오트','하티','플랫','화이트','위트']
toasting = ['O','X']
source = ['랜치&어니언','올리브오일&소금&후추','스위트칠리','바베큐&마요네즈','핫칠리','랜치&스위트칠리']


# charge 변수로 잔돈을 초기화 시킴.
charge = -1

# 손님 주문 사항 기록(변동값)- 주문 샌드위치 항목과 개수, 샌드위치 내용물 변경용()
menu_list = {"이탈리안비엠티": 0, "터키": 0, "에그마요": 0, "스테이크": 0, "쉬림프": 0, "BLT": 0}



# 화면에 선택할 메뉴 출력

def printMenu(): # 메뉴를 출력해주는 매개변수 선언
    print("\n＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊")
    print("         ɢᴏᴏᴅ-ᴍᴏʀɴɪɴɢ•°♪♪")
    print("＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊\n")
    print("     1. 샌드위치 메뉴 선택\n     2. 주문 내역 확인\n     3. 메뉴 옵션 변경\n     4. 메뉴 취소\n     5. 결제\n     6. 종료\n ")
    print("＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊┈┈┈┈＊\n")

#샌드위치 종류 출력

def printSandwichMenu(): # 샌드위치 종류를 출력해주는 매개변수를 선언
    print("\n\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n       [Sandwich Menu]\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n   이탈리안비엠티   6200원\n   터키             5400원\n   에그마요         5800원\n   스테이크         7200원\n   쉬림프           6300원\n   BLT              6000원\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n")

# 주문할 샌드위치 메뉴와 개수 입력

def selectMenu():  # 메뉴를 선택하는 매개변수 선언
    printSandwichMenu()  # 샌드위치를 택할 수 있도록  샌드위치 종류를 보여줌.
    while True:
        enter_menu = input("주문하실 샌드위치를 입력해주세요. ┈┈┈> ").upper().replace(" ","")
        # 샌드위치명을 입력해서 주문할 수 있게 함.
        if (enter_menu == ''):  # 만약 입력하지 않으면 메뉴를 다시 입력하도록 설명을 보여줌.
            print("메뉴를 다시 입력해주세요!")
        elif enter_menu in ["이탈리안비엠티", "터키", "에그마요", "스테이크", "쉬림프", "BLT"]:  # 샌드위치 종류 중 하나 선택
            # 선택한 샌드위치의 수량을 정수로 입력받아 변수에 넣어줌.
            quantity = int(input(" 몇 개 주문하시겠습니까?"))
            menu_list[enter_menu] += quantity  # 입력한 샌드위치명에 수량을 증가시킴.
            break  
        else:  # 샌드위치 메뉴판에 없는 메뉴를 입력했을 때 안내해줌.
            print("메뉴를 다시 입력해주세요!")

#샌드위치 주문 내역 출력

def checkOrder():  # 주문내역을 확인하는 매개변수 선언
    # if(menu_list in ["이탈리안비엠티","터키","에그마요","스테이크","쉬림프","BLT"]):
    #     print("\n")
    if(menu_list["이탈리안비엠티"] > 0):  # 각 선택한 메뉴와 선택한 수량을 출력시켜줌
        print("\n이탈리안비엠티   %d개" % menu_list["이탈리안비엠티"])

    if(menu_list["터키"] > 0):
        print("\n터키   %d개" % menu_list["터키"])

    if(menu_list["에그마요"] > 0):
        print("\n에그마요   %d개" % menu_list["에그마요"])

    if(menu_list["스테이크"] > 0):
        print("\n스테이크   %d개" % menu_list["스테이크"])

    if(menu_list["쉬림프"] > 0):
        print("\n쉬림프   %d개" % menu_list["쉬림프"])

    if(menu_list["BLT"] > 0):
        print("\nBLT   %d개" % menu_list["BLT"])

#총 가격 계산 및 금액 지불


# 6개의 메뉴 중 주문한 샌드위치와 수량에 맞게 계산해서 총 구매금액에 넣어줌
def calculatePrice(menu1, menu2, menu3, menu4, menu5, menu6):
    raw_total_price = (6200*menu1) + (5400*menu2) + \
        (5800*menu3) + (7200*menu4) + (6300*menu5) + (6000*menu6)
    print("\n\n합계 : %d" % raw_total_price,'원 입니다.')  # 총 구매금액을 출력
    conn = sqlite3.connect(path + '/customer.sqlite')
    cur = conn.cursor()
    ans_2 = input('회원이십니까?(Y/N) ┈┈┈> ').upper()
    if ans_2 == 'Y':
        cust_tell = input('전화번호를 입력해주세요 ┈┈┈> ')
        ans = input('포인트를 사용하시겠습니까?(Y/N) ┈┈┈>').upper()
        if ans == 'Y':
            cur.execute(f"select * from GUEST where tel = '{cust_tell}'") 
            search = cur.fetchone() # GUEST의 tel 부분에서 cust_tell과 같은값을 찾아서 search에 저장.
            print(search[2],'의 포인트가 있습니다.') # point 항목인 search[2]를 출력하여 적립금이 얼마나 있는 지 출력.
            ans_1 = int(input('포인트를 얼마나 사용하시겠습니까? ┈┈┈>'))
            point_use = list(search) # 튜플형식인 search를 리스트로 바꿔 값을 변경할 수 있도록 함.
            if point_use[2] >= ans_1: # 가지고 있는 적립금인 point_use[2]이 사용하려는 포인트인 ans_1보다 같거나 커야하므로 조건부여 
                point_1 = point_use[2] - ans_1 # 적립금 사용은 가지고 있는 적립금 - 사용하려는 적립금 값을 저장
                sql = f'update GUEST set point = ? where tel = ? ' 
                cur.execute(sql,(point_1,cust_tell)) 
                # GUEST에서 tel이 cust_tell에서 입력한 번호와 같은 곳에 사용하고 남은 적립금인 point_1을 저장
                total_price = raw_total_price - ans_1 #최종 결제금액 = 총 구매금액에서 - 사용하려는 적립금

            else:
                print('사용가능한 포인트 금액을 넘었습니다.') 
                ans_1 = 0            
                total_price = raw_total_price - ans_1
                # else를 통해 가지고 있는 적립금이 사용하려는 적립금보다 작은경우 사용하는 적립금을 0값으로 주고 넘어감.
        elif ans == 'N':
            ans_1 = 0
            total_price = raw_total_price
            # 적립금을 사용한다고 하지 않을 경우도 ans_1값을 부여
        else:
            print('맞는 값을 입력해주세요.')
            return
    elif ans_2 == 'N':
        ans_1 = 0
        total_price = raw_total_price
    else:
        print('형식에 맞는 값을 입력하세요.')
    print("%d원 이상의 돈을 지불하세요!" % total_price)
    input_price = int(input("지불할 금액 : "))  # 지불할 금액을 입력
    while total_price > input_price:  # 지불한 금액이 구매금액보다 작으면
        print("%d원 이상의 돈을 지불하세요" % total_price)  # 구매금액 이상의 돈을 지불하라는 내용을 출력
        input_price = int(input("지불할 금액 : "))
    
    charge = input_price - total_price
    
    point_2 = round(total_price*0.05,-1)
    if ans_2 == 'Y': # 회원일 경우
        if ans == 'Y': #포인트 사용할 경우
            point_3 = point_2 + point_1
            sql = f'update GUEST set point = ? where tel = ? ' 
            cur.execute(sql,(point_3,cust_tell))          # 결제 금액의 0.05%만큼 적립 포인트는 10의 자리까지 반올림해서 보여줌.
            past_order = [k for k, v in menu_list.items() if v != 0] 
            # 가장 최근 주문목록을 만들기 위해 menu_list의 velue가 0이 아니면 주문을 한 것이므로 0이 아닌 키값을 가져온다.
            order = ','.join(past_order)
            # past_order에서 리스트로 할 경우 여러개를 주문했을 때 전체가 아닌 한가지만 출력되서 
            # join을 통해 리스트를 ','을 추가한 문자 형식으로 변환
            sql = f'update GUEST set past_order = ? where tel = ? ' 
            cur.execute(sql,(order,cust_tell))
            print(past_order,'을 결제하셨습니다.')  #order을 통해 만든 값을 최근 주문값인 past_order에 입력   
            # 문제점 발견 종료하지 않고 계속 구매를 반복할 경우 이전 구매목록이 계속 누적됨.
        
        elif ans == 'N': #포인트 사용하지 않을경우
            cur.execute(f"select * from GUEST where tel = '{cust_tell}'") 
            search = cur.fetchone()
            point_use = list(search)
            point_3 = point_2 + point_use[2]
            sql = f'update GUEST set point = ? where tel = ? ' 
            cur.execute(sql,(point_3,cust_tell))
            past_order = [k for k, v in menu_list.items() if v != 0]
            order = ','.join(past_order)
            sql = f'update GUEST set past_order = ? where tel = ? ' 
            cur.execute(sql,(order,cust_tell))
            print(past_order,'을 결제하셨습니다.')
    elif ans_2 == 'N': # 회원이 아닐경우
        print('---------------------------------------')
        # Y를 선택할 경우 포인트는 사용하고 남은 포인트에 기본 적립 포인트 적립
        # N을 선택할 경우 남아있던 포인트에 기본포인트 적립
        # else의 경우 그냥 끝냄
    if ans_2 == 'Y':
        print("지불 완료되셨습니다.")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("총  합계       : %d" % raw_total_price)
        print("지불한 금액    : %d" % input_price)
        print("사용한 포인트 : %d" % ans_1) # ans_1값에 오류가 나지 않기 위해 위에서 ans_1에 0값을 부여한 것이였다.
        print("잔돈은 %d원 입니다." % charge)
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("적립 포인트 : %d" % point_2)
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    elif ans_2 == 'N': # 적립포인트부분 제거함.
        print("지불 완료되셨습니다.")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("총  합계       : %d" % raw_total_price)
        print("지불한 금액    : %d" % input_price)
        print("사용한 포인트 : %d" % ans_1) 
        print("잔돈은 %d원 입니다." % charge)
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    if (charge//5000 > 0):
        print("5000원: %d" % (charge//5000))
        charge -= (charge//5000)*5000

    if (charge // 1000 > 0):
        print("1000원: %d" % (charge//1000))
        charge -= (charge//1000)*1000

    if (charge // 500 > 0):
        print("500원: %d" % (charge//500))
        charge -= (charge//500)*500

    if (charge // 100 > 0):
        print("100원: %d" % (charge//100))
        charge -= (charge//100)*100

    if (charge // 50 > 0):
        print("50원 : %d" % (charge//50))
        charge -= (charge//50)*50

    if (charge // 10 > 0):
        print("10원 : %d" % (charge//10))
        charge -= (charge//10)*10   
    

    conn.commit()
    conn.close()  #위에 변경된 데이터를 저장후 종료


# 샌드위치의 빵, 토스팅, 소스의 옵션을 변경

def updateMenu():
    sname = input('변경하실 샌드위치를 입력해주세요. ----> ').upper().replace(" ","")
    idx = -1
    for i, item in enumerate(sandwich):
        if item['sname'] == sname:
            idx = i
            while True:
                update_s = input('\n변경할 옵션 - bread, toasting, sauce, exit(종료) ┈┈┈> ')
                if update_s == 'bread':
                    print('\n1. 파마산오레가노, 2. 허니오트, 3. 하티, 4. 플랫, 5. 화이트, 6. 위트')
                    ans = int(input('\n바꾸고 싶은 빵의 번호를 입력하세요. ┈┈┈> '))
                    if ans not in range(1,7):
                        print('맞는 숫자값을 입력하세요!')
    # 변경할 옵션을 고르면 print를 통해 해당값에 맞는 선택지를 부여하고 ans를 통해 번호를 int형태로 입력받음.
    # 입력받은 값을 range함수를 통해 원하는 숫자 범위안에 있는지 확인 후 없으면 맞는 숫자값을 입력하도록 보여줌.
                    else:
                        sandwich[idx][update_s]=bread[ans-1]
                    print(sandwich[idx][update_s],'으로 변경되었습니다.') 
    # 위에서 idx = i로 했기 때문에 입력한 sname과 리스트 안 딕셔너리들의 'sname'이 같은 값의 딕셔너리에서 
    # update_s를 통해 변경할 부분을 선택하고 [ans-1]을 통해 선택지에서 선택한 값과 변경되는 값이 같도록 한다.  
                elif update_s == 'toasting':
                    print('1.O,2.X')
                    ans = int(input('toasting하시려면 1번을 아니면 2번을 누르세요. ----> '))
                    if ans not in range(1,3):
                        print('맞는 숫자값을 입력하세요!')
                    else:
                        sandwich[idx][update_s]=toasting[ans-1]
                    print(sandwich[idx][update_s],'으로 변경되었습니다.')
                elif update_s == 'sauce':
                    print('1.랜치&어니언','2.올리브오일&소금&후추','3.스위트칠리','4.바베큐&마요네즈','5.핫칠리','6.랜치&스위트칠리')
                    ans = int(input('바꾸고 싶은 소스의 번호를 입력하세요. ----> '))
                    if ans not in range(1,7):
                        print('맞는 숫자값을 입력하세요!')
                    else:
                        sandwich[idx][update_s]=source[ans-1]
                    print(sandwich[idx][update_s],'으로 변경되었습니다.')        
                elif update_s == 'exit':
                    break
            print(sandwich[idx],'으로 변경되었습니다.')
            break
    if idx == -1:
        print('존재하지않는 메뉴입니다! ')

#메뉴를 취소할 경우:
#고객 주문 리스트(:menu_list)에 취소 메뉴 이름(:sname)이 있을 경우
#해당 품목 주문(:menu_list[sname])을 취소(0)한다.
def deleteMenu(menu_list):
    sname = input('취소하실 메뉴를 입력해주세요. ┈┈┈> ').upper().replace(" ","")
    if menu_list.get(sname) != 0 and sname in menu_list:
       menu_list[sname] = 0
    else:
        print('존재하지 않은 데이터 입니다.')


#Main Code
def main_code():
    while True:
        printMenu()
        menu_select = input("메뉴를 선택해주세요 ┈┈┈> ")

        if menu_select == '1':
            selectMenu()

        elif menu_select == '2':
            checkOrder()

        elif menu_select == '3':
            updateMenu()

        elif menu_select == '4':
            deleteMenu(menu_list)

        elif menu_select == '5':
            #주문 하지 않을 경우
            if list(menu_list.values()) == [0, 0, 0, 0, 0, 0]:
                print("먼저 주문해 주세요! ")
                continue
            calculatePrice(menu_list["이탈리안비엠티"], menu_list["터키"],
                           menu_list["에그마요"], menu_list["스테이크"],
                           menu_list["쉬림프"], menu_list["BLT"])

        elif menu_select == '6':
            break
        else:
            #1~4 중 하나를 선택하지 않은 경우
            print("메뉴를 잘못 입력하셨습니다.\n1 ~ 6중 하나를 선택해주세요. ")