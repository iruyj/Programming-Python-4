class Celebrity:
    def __init__(self,name):    #필수 생성자 함수
        self.name=name

    def set_name(self, name):
        self.name=name

    def set_entertainment(self, entertainment):
        self.entertainment=entertainment

    def __str__(self):      #쉽게 출력하기 위해서
    #   <__main__.Celebrity object at 0x00000210E8FF8700> 이거였음
    #     #주로 print(객체명)로 객체를 출력할때 자동호출되어서 문자열을 리턴함
        return f"이름: {self.name}\t소속사: {self.entertainment}"

class Talent(Celebrity):
    def __init__(self,name):
        super().__init__(name)

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        return super().__str__()+f'\t드라마: {self.drama}'
        # return f'이름: {self.name}\t소속사: {self.entertainment}\t드라마: {self.drama}'

class Singer(Celebrity):
    def __init__(self,name, song):
        super().__init__(name)
        self.song = song

    def __str__(self):
        return super().__str__()+ f'\t노래: {self.song}'


IU = Celebrity('이지은')        #new Celebrity() in java
IU.set_entertainment('이담')
print(IU.name, IU.entertainment)
print(IU)

이진호 = Celebrity('이진호')
이진호.set_entertainment('SM C&C')
print(이진호)

이광수=Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)

현진 = Singer('현진','신')
필릭스 = Singer('필릭스','Back Door')
현진.set_entertainment('JYP')
필릭스.set_entertainment('JYP')

print('----------그룹---------------')
스트레이키즈 = []
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)

for 멤버 in 스트레이키즈:
    print(멤버)