from recipebook import RecipeBook  #선언했는데 사용하지 않았을때 회색으로 나타남
def print_menu():
    print('\n------------------------')
    print('1. 레시피 검색')
    print('2. 레시피 추가하기')
    print('3. 재료로 검색하기')
    print('4. 전체 레시피 보여주기')
    print('5. 종료하기')
    num = input('>> 메뉴를 선택하세요 :')
    return num

def main():

    while True:
        # 재료 여러개로 검색, 레시피 수정하기 기능
        num = print_menu()
        recipebook_204 = RecipeBook()
        if num == '1':
            # 레시피 검색
            recipebook_204.search_recipe()
        elif num== '2':
            # 레시피 추가
            recipebook_204.add_recipe()
        elif num== '3':
            # 재료로 검색
            recipebook_204.search_ingredient()
        elif num== '4':
            # 전체 레시피 보여주기
            recipebook_204.show_recipe()
        elif num== '5':
            # 종료
            break
        else:
            print('다시 입력하세요')

if __name__ == '__main__':  # __name__ : 파이썬 내장 변수
# main이 name일 때 실행한다.
    main()