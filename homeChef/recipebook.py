from recipe import Recipe  # 레시피 파일에서 레시피 클래스를 가져온다

class RecipeBook:
    def __init__(self):
        self.recipe_list = []
        self.init_recipe()

    def add_recipe(self):
        # 추가할 레시피 이름 입력받기
        name = input('레시피 이름 >> ')
        # 중복 체크
        for recipe in self.recipe_list:
            # 중복되는 레시피가 있으면
            if name == recipe.name:
                # 중복된다고 알려주기
                print('중복됩니다-')
                return

        # 중복되는 레시피가 없으면
        new_recipe = Recipe(name)  # 레시피 생성하기
        new_recipe.set_recipe()
        # 레시피 리스트에 생성한 레시피 추가
        self.recipe_list.append(new_recipe)

    # 레시피 전체 보여주기
    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index + 1}')
            print(recipe)

    # 레시피북에서 레시피 검색하기
    def search_recipe(self):
        searched_recipe=[] #찾아진 레시피를 담는 변수
        name = input('>> 원하는 레시피를 검색 : ')

        for recipe in self.recipe_list:
            if name == recipe.name: #검색한 레시피이름과 같은 레시피가 있으면
                print(recipe)   #보여준다
                searched_recipe.append(recipe) #담는다.
                # return
        if len(searched_recipe)==0:
            answer = int(input('>> 찾는 레시피가 없습니다. 추가하시겠습니까? (1:예 | 0:아니오)'))
            if answer:  #python에서 true는 1이므로 생략해도 가능
                self.add_recipe()
            else:
                return
    
    # 재료로 해당되는 레시피 찾기
    def search_ingredient(self):
        # set : 중복 제거하고 특정값을 포함하는지 확인할때 사용

        # 빈 set 생성 -> 재료를 중복 제거해서 담은 set
        all_ingredient = set()
        # 레시피북에 있는 레시피의 재료들 set에 넣기
        for recipe in self.recipe_list:
            for ingredient in recipe.ingredient:
                all_ingredient.add(ingredient)  # 딕셔너리의 key만 들어감
        # 모든 재료를 보여주기
        for index, ing in enumerate(all_ingredient):
            print(f'{index+1}. {ing}')

        # 찾을 재료의 이름 검색
        search_num = int(input('>> 사용할 재료번호를 입력하세요 :'))
        search_ingreredient = list(all_ingredient)[search_num-1]
        # 검색한 재료가 들어있는 레시피를 찾는다
        for recipe in self.recipe_list:
            if search_ingreredient in recipe.ingredient:
                # 검색한 재료가 포함되는 레시피가 있으면 모두 보여주기
                print(recipe)

    # 기본 레시피 초기화
    def init_recipe(self):
        떡볶이 = Recipe('떡볶이')
        떡볶이.peple =2
        떡볶이.ingredient ={'떡':'200','고추장':'100','어묵':'100','양파':'20'}
        떡볶이.video = 'youtube.com'

        카레 = Recipe('카레')
        카레.peple =2
        카레.ingredient ={'카레가루':'50','감자':'200','당근':'100'}
        카레.video ='youtube.com'

        파스타 =Recipe('파스타')
        파스타.contents='재료를 넣는다. 파스타를 만든다'
        파스타.ingredient ={'면':'100','소스':'30'}
        
        self.recipe_list.append(떡볶이)
        self.recipe_list.append(카레)
        self.recipe_list.append(파스타)

