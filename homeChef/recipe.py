class Recipe:
    def __init__(self, name):
        # 재료, 재료의 개수(양)
        self.ingredient = {}  # 빈 딕셔너리 생성
        # 내용
        self.contents = ''
        # 이름
        self.name = name
        # 몇 인분
        self.peple = 1
        # 영상 링크
        self.video = ''

    def set_contents(self):
        content = input('레시피 내용 입력 : ')
        self.contents = '-입력된 정보가 없습니다-' if content=='' else content

    def set_peple(self):
        peple = input('몇 인분인가 : ')
        self.peple = 1 if peple == '' else peple

    def set_video(self):
        video = input('참고 레시피영상 주소 : ')
        self.video = '입력된 주소가 없습니다' if video=='' else video

    def set_ingredient(self):
        print('재료입력 끝났으면 엔터 누르기 : (재료 입력예시: 감자 100) ')
        while True:
            ingredient = input('재료 입력  >> ')

            if ingredient == '': break
            ingredient_name, ingredient_gram = ingredient.split(' ')
            self.ingredient[ingredient_name] = ingredient_gram #딕셔너리 키에 맞는 곳에 값을 추가한다/ 키가 딕셔너리에 없으면 키도 자동으로 추가된다
            # {'감자':'200', '당근':'100'}

    def set_recipe(self):
        self.set_peple()
        self.set_ingredient()
        self.set_contents()
        self.set_video()

    def __str__(self):
        return f'---{self.name} 레시피-----\n양: {self.peple}인분\n정보: {self.contents}\n영상링크: {self.video}\n재료: {self.ingredient}'
    
# 카레 = Recipe('카레')
# 카레.set_recipe()
# print(카레)