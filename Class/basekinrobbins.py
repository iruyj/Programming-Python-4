class Icecream:
    def __init__(self, name):
        self.name = name

    def set_explanation(self,explanation):
        self.explanation = explanation

    def __str__(self):
        return f'이름: {self.name}'

아이스홈런볼 = Icecream('아이스홈런볼')
아이스홈런볼.set_explanation('초콜릿 아이스크림과 바닐라 아이스크림 ')

뉴치케 = Icecream('뉴욕치즈케익')
# print(뉴치케)

요거트31 = Icecream('31요거트')
# print(요거트31)

바람과함께사라지다 = Icecream('바람과함께사라지다')
# print(바람과함께사라지다)

class Order:
    #클래스 변수 만들기(static, 상수아님-변할수있음)_튜플: 바뀌지 않기위해
    #접근 : 클래스이름.클래스변수명
    _CATEGORIES = ('싱글레귤러','더블레귤러','파인트')
    _PRICES = (3200, 6200, 8200)

    def __init__(self):
        self.set_cateries()     #파인트, 패밀리 등 사이즈 선택 호출
        self.menu = []          #기본 매장메뉴 선언
        self.order_menu = []    #주문한 메뉴 저장
        #메뉴
        self.init_menu()        #기본 메뉴 초기화

    def __str__(self):
        for icecream in self.order_menu:
            print(' '*5,icecream)       #마지막에 주문한 메뉴 종류 출력

    def set_cateries(self):
        #인텍스와 데이터 같이 꺼내는 방법 enumerate(리스트명)
        for index,category in enumerate(Order._CATEGORIES):
            print(index+1,category)     #사이즈 카테고리 종류 출력
        category_num = input('종류를 골라주세요 : ')
        self.category = int(category_num)   

    def init_menu(self):    #메뉴 초기화
        #아까에 만들었던 클래스의 객체를 리스트에 저장
        self.menu.append(Icecream('뉴욕치즈케익'))
        self.menu.append(Icecream('31요거트'))
        self.menu.append(Icecream('바람과 함께 사라지다'))

    def show_menu(self): # 선택할 메뉴 종류 보여주기
        for i,ice in enumerate(self.menu):
            print(i+1,ice)

    def order(self):
        self.show_menu()    #고를 메뉴 보여주기
        # 고를 수 있는 개수에 따라 반복
        for _ in range(self.category):  #카테고리 길이만큼 반복 _ : 반복만 하지 값 안가져와도 될때
            #   메뉴 선택
            icecream = input('아이스크림을 골라주세요 : ')
            icecream = int(icecream)
            self.order_menu.append(self.menu[icecream-1])   #주문한 메뉴에 추가하자

        #종류 출력
        print('-'*10 + '주문 내역입니다'+'-'*10)
        print(' '*5,Order._CATEGORIES[self.category-1],' : ', str(Order._PRICES[self.category-1])+'원')
        #주문한 메뉴 출력
        self.__str__()

order = Order()
order.order()
