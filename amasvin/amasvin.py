class Drink:
    _CUPS = ('레귤러', '점보')  # 기본 : 레귤러
    _ICES = ('0%', '50%', '100%', '150%')  # 100% 기본
    _SUGARS = ('0%', '50%', '100%', '150%')  # 100% 기본

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0  # 레귤러
        self.ice = 2  # 100%
        self.sugar = 2  # 100%

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):  # 컵종류 보여주기
            print(index + 1, ':', cup)
        cup = input('컵사이즈 선택 : ')
        if cup == '':  # 그냥 엔터쳤을 때 레귤러 들어가기
            self.cup = 0
        else:  # -1해서 인덱스 조정
            self.cup = int(cup) - 1
        self.price = self.price + 500 if cup == '2' else self.price + 0  # 가격 조정

    def set_ice(self):
        # 얼음량 종류 보여주기
        for index, ice in enumerate(Drink._ICES):
            print(index + 1, ':', ice)

        # 선택하기
        ice = input('얼음량 선택 : ')
        # if ice == '':  # 그냥 엔터쳤을 때 100% 들어가기
        #     self.ice = 0
        # else:
        #     ice = int(ice)-1
        #     self.ice = ice         #self.ice에 설정하기

        # 위의 이프문 한줄처리
        self.ice = 2 if ice == '' else int(ice) - 1

    def set_sugar(self):
        # 당도 종류 보여주기
        for index, sugar in enumerate(Drink._SUGARS):  # 컵종류 설정
            print(index + 1, ':', sugar)

        sugar = input('당도 조절 선택 :')
        self.sugar = 2 if sugar == '' else int(sugar) - 1

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}\t당도: {Drink._SUGARS[self.sugar]}'


class Coffee(Drink):
    pass


class Bubbletea(Drink):
    _PEARLS = ('타피오카펄', '화이트', '알로에', '젤리')

    def __init__(self, name, price):
        # 부모초기화 호출
        super().__init__(name, price)
        self.pearl = 0

    def set_pearl(self):
        # 펄 종류 보여주기
        for index, pearl in enumerate(Bubbletea._PEARLS):  # 컵종류 설정
            print(index + 1, ':', pearl)
        # 선택하기
        pearl = input('당도 조절 선택 :')
        self.pearl = 2 if pearl == '' else int(pearl) - 1  # self.peal에 넣기

    def order(self):
        # 부모 클래스 order 함수 호출
        super().order()
        # set_pearl 호출
        self.set_pearl()

    def __str__(self):
        # 부모 클래스 str 호출, + 펄 출력
        return super().__str__() + f'\t펄 : {Bubbletea._PEARLS[self.pearl]}'


class Order():
    def __init__(self):
        self.menu = [] #self.menu 매장에 있는 음료수 전체
        self.init_menu() #init_menu()
        self.order_menu =[] #self.order_menu 내가 고른 메뉴들

    def init_menu(self):
        one = Coffee('카페모카',2500)
        two = Bubbletea('오레오 쉐이크',3900)
        three = Bubbletea('타로 밀크티',3300)
        self.menu.append(one)
        self.menu.append(two)
        self.menu.append(three)

    def show_menu(self):
        for index, menu in enumerate(self.menu):
            print(f'{index + 1} : {menu.name}\t{menu.price}원')

    def sum_price(self):
        sum =0
        for i in self.order_menu:
            sum += i.price
        return sum

    def order_drink(self):
        while True:
            self.show_menu()  #메뉴 보여주기
            drink = input('메뉴 선택 :')   # 메뉴 선택
            drink = int(drink)-1
            new_drink = self.menu[drink]
            new_drink.order()  #옵션 선택
            self.order_menu.append(new_drink) #self.order_menu에 추가
            is_add = input('더 주문하시겠습니까(n:종료)')
            if is_add =='n':
                break
        print(self) #주문내역 보여줌

    def __str__(self):
        s = '-' * 20+'주문 내역'+ '-'* 20+'\n'#주문내역 제목보여주기
        for drink in self.order_menu:
            s+=str(drink)+'\n'
        s += f'\n총금액 : {self.sum_price()}원' #총 합계 가격 보여주기
        return s


# drink = Drink('밀크티',2500)
# drink.order()
# print(drink)

# bb = Bubbletea('흑당 버블티', 3900)
# bb.order()
# print(bb)

order = Order()
order.order_drink()