# #자료형------------------------------------------------------------------------
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# #문자열 자료형-----------------------------------------------------------------
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# #참 / 거짓 -------------------------------------------------------------------
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)

#변수 --------------------------------------------------------------------------
# name="연탄"
# animal ="강아지"
# age=4
# hobby="산책"
# is_adult=age>=3 #true or faulse
#
# print(f"우리집 {animal}의 이름은 연탄")
# print("연탄이는"+ str(age)+"솰 좋아하는 건 "+hobby)
# print("연탄이는 어른인과? ", str(is_adult))

# #퀴즈1 변수를 이용해 다음 문장 출력   ---------------------------------------------
# # 변수명:station   / 변수값: 사당,신도림,인천공항 순서대로 입력
# # 출력 문장 : xx행 열차가 들어오고 있습니다.
# station = "사당"
# print(station, "행 열차가 들어오고 있습니다")
# station = "신도림"
# print(station, "행 열차가 들어오고 있습니다")
# station = "인천공항"
# print(station, "행 열차가 들어오고 있습니다")

#연산자    ---------------------------------------------------------------------
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)
#
# print(2**3)
# print(5%3)
# print(5//3)
# print(10%3)
# print(10//3)
#
# print(10>3)
# print(4>=7)
# print(10<3)
# print(5<=5)
#
# print(3==3)
# print(4==2)
# print(5==3)

# print(1!=3)
# print(not(1!=3))
#
# print((3>0) and (3<5))
# print((3>0) & (3<5))
#
# print((3>0) or (3<5))
# print((3>0) or (3>5))
#
# print(5>4>3)
# print(5>4>7)

#간단한 수식 --------------------------------------------------------------------
# print(2+3*4)    #14
# print((2+4)*4)  #24
# num=2+3*4
# print(num)  #14
# num=num+2
# print(num)  #16
# num+=2
# print(num)  #18
# num*=2
# print(num)  #36
# num/=2
# print(num)  #18
# num-=2
# print(num)  #16
# num%=2
# print(num)  #0

#숫자 처리 함수-------------------------------------------------------------------
# print(abs(-5))
# print(pow(4,2))
# print(max(5,12))
# print(min(5,12))
# print(round(3.14))
# print(round(4.99))
#
# from math import *
# print(floor(4.99))  #내림 4
# print(ceil(3.14))   #올림 4
# print(sqrt(16))     #루트 4

#랜덤함수   ---------------------------------------------------------------------
from random import *

# print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10)  #0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) #0 ~ 10 미만의 임의의 값 생성
# print(int(random()*10)+1)   #1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1)   #1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1)   #1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1)   #1 ~ 10 이하의 임의의 값 생성

# #로또 45까지 출력
# print(int(random()*45)+1)   #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1)   #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1)   #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1)   #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1)   #1~45 이하의 임의의 값 생성
#
# print(randrange(1,45))  #1~45 미만의 임의의 값 생성
# print(randint(1,45))  #1~45 이하의 임의의 값 생성

# #퀴즈 2 ----------------------------------------------------------------------
# #월 4회 스터디, 3번은 온라인 1번은 오프라인
# #조건 1 : 랜덤으로 날짜를 뽑아야함
# #조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# #조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
# date = randint(4,28)
# print(f"오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")

#문자열    ----------------------------------------------------------------------
# sentence ="나는 소년"
# print(sentence)
# sentence="파이썬 이즈 이지"
# print(sentence)
# sentence="""
# 나는 소년이고,
# 파이썬은 쉽다
# """
# print(sentence)

#슬라이싱   ---------------------------------------------------------------------
# jumin = "990121-1234567"
# print("성별 : "+jumin[7])
# print("년도 : "+jumin[:2])
# print("월 : "+jumin[2:4])
# print("일: "+jumin[4:6])
#
# print("생년월일 : "+jumin[:6])
# print("뒤 7자리 : "+jumin[7:])
# print("뒤 7자리 : "+jumin[-7:])

# #문자열 처리함수   -------------------------------------------------------------
# python="Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())  #대문자인지 판별
# print(len(python))
# print(python.replace("Python", "Java"))
#
# index=python.index("n")
# print(index)
# index = python.index("n",index+1)   #두번째 n의 위치
# print(index)
#
# print(python.find("Java"))      #find  : 원하는 값이 없으면 -1 반환
# # print(python.index("Java"))   #index : 원하는 값이 없으면 오류 반환
# print("hi")
#
# print(python.count("n"))    #n이 몇번 등장하는지

#문자열포맷(출력)  ---------------------------------------------------------------
# #방법1
# print("나는 %d살입니다."% 20)
# print("나는 %s을 좋아함"% "python")
# print("Apple 은 %c로 시작"% "A")
# print("나는 %s살입니다."% 20)
# print("나는 %s색과 %s색을 좋아한다!."% ("파란", "빨간"))

# #방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아한다!.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아한다!.".format("파란", "빨간"))

# #방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="red"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="red",age=20))

# #방법4
# age=20
# color="darkgreen"
# print(f"나는 {age}살이며, my favorit color is {color}.")

#탈출문자   ---------------------------------------------------------------------
# #\n : 줄바꿈
# print("백문이 불여일견\n 백견이 불여일타")
#
# #\"\" :문장 내에서 따옴표 '',"" 표시
# print("저는 \"미림여정\" 2학년입니다.")
#
# #\\ : 문장 내에서 하나의 역슬래쉬 \
# print("C:\\projects\\nadoCoding\\venv\\Scripts\\python.exe")
#
# #\r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
#
# #\b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")
#
# #\t : 탭
# print("Red\tApple")

#퀴즈3    ----------------------------------------------------------------------
#사이트별로 비밀번호를 만들어주는 프로그램 작성
# 예) http://naver.com
#규칙 1 : http:// 부분은 제외 => naver.com
#규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

#생성된 비밀번호 : nav51!
#
# url = "http://naver.com"
# pw=url.replace("http://","")
# dot_index = url.index(".")
# pw= url[:dot_index]
# print("생성된 비밀번호 : "+pw[:3]+str(len(pw))+str(pw.count("e"))+"!")

#리스트   ----------------------------------------------------------------------
# subway=[10,20,30]
# print(subway)
#
# #조세호 어디 있는지 세기
# subway=["유재석","조세호","박명수"]
# print(subway.index("조세호"))
#
# #맨뒤에 추가
# subway.append("하하")
# print(subway)
#
# #원하는 index 자리에 추가
# subway.insert(1,"정형돈")
# print(subway)
#
# #맨뒤에 하나 빼기
# print(subway.pop())
# print(subway)
#
# #유재석 몇번 나오는지 세기
# subway.append("유재석")
# print(subway.count("유재석"))
#
# #정렬
# num_list=[1,6,7,3,9,0]
# num_list.sort()
# print(num_list)
#
# #거꾸로 정렬
# num_list.reverse()
# print(num_list)
#
# #모두 지우기
# num_list.clear()
# print(num_list)
#
# #다양한 자료형과 함께 사용 가능
# mix_list=["조세호",20,True]
# print(mix_list)
#
# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

#사전 -------------------------------------------------------------------------
from nadoCoding.travel import thailand

cabinet={3:"유재석",100:"김태호"}
# print(cabinet[3]) #열쇠의 번호를 인덱스로 출력
# print(cabinet[100])
#
# print(cabinet.get(3))   #값을 가져오는 방법
# print(cabinet[5])     #없는 키 출력 시 오류 반환
# print(cabinet.get(5))   #없는 키 출력 시 None 반환이나 원하는 문자 반환
# print(cabinet.get(5,"사용가능"))
# print("hi")

# print(3 in cabinet) #True
# print(5 in cabinet) #false
#
# cabinet= {"3-1":"공도윤","4-18":"전유리"}
# print(cabinet["3-1"])
# print(cabinet["4-18"])
#
# #새로운 값 추가
# print(cabinet)
# cabinet["3-1"]="이은교" #값 업데이트
# cabinet["4-19"]="정나라"
# print(cabinet)
# #
# # #값 지우기
# # del cabinet["3-1"]
# # print(cabinet)
#
# #키만 출력
# print(cabinet.keys())
#
# #value들만 출력
# print(cabinet.values())
#
# #key, value 둘다 출력
# print(cabinet.items())
#
# #전부 비우기
# cabinet.clear()
# print(cabinet)

#튜플 --------------------------------------------------------------------------
# menu=("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])
#
# # menu.add("생선까스") #튜플은 걊 추가 및 변경이 불가함
#
# # name="나미림"
# # age =17
# # hobby="코딩"
# # print(name,age,hobby)
#
# name, age, hobby="나미림",17,"코딩"
# print(name,age,hobby)

#세트     ---------------------------------------------------------------------
# my_set= {1,2,3,3,3}
# print(my_set)
#
# java={"유재석","나미림","탈미림"}
# python=set(["유재석","박명수"])
#
# #교집합 (java 와 python 둘다 가능한 개발자)
# print(java & python)
# print(java.intersection(python))
#
# #합집합 (java도 할수 있거나 python도 할수있는 개발자)
# print(java | python)
# print(java.union(python))
#
# #차집합 (java는 할 줄 알지만 python은 할 줄 모르는 개발자)
# print(java-python)
# print(java.difference(python))
#
# #python 할 줄 아는 사람이 늘어남
# python.add("미리민")
# print(python)
#
# #java를 잊었어요
# java.remove("탈미림")
# print(java)

#자료구조의 변경   ---------------------------------------------------------------
#커피숍
# menu={"커피","우유","주스"}
# print(menu,type(menu))
#
# menu= list(menu)
# print(menu, type(menu))
#
# menu=tuple(menu)
# print(menu, type(menu))
#
# menu=set(menu)
# print(menu, type(menu))

#퀴즈4    ---------------------------------------------------------------------
#파이썬 코딩 대회 주최 / 참석율 높이기 위해 댓글 이벤트 진행 / 작성자 중 추첨,
#한명은 치킨, 3명은 커피 쿠폰

#조건 1: 편의상 댓글은 20명 작성 / 아이디는 1~20이라고 가정
#조건 2 : 댓글 내용과 상관없이 무작위로 추첨, 중복 불가
#조건 3 : random 모듈의 shuffle고 sample활용

# from random import *
# id= range(1,21)
# id=list(id)
# shuffle(id)
# getid= sample(id,4)
#
# print('-- 당첨자 발표 --')
# print("치킨 당첨자 : {0}" .format(getid[0]))
# print(f"치킨 당첨자 : [{getid[1]}, {getid[2]}, {getid[3]}]",)
# print("-- 축하합니다 --")

#if문    -----------------------------------------------------------------------
# weather = input("오늘 날씨 : ")
# if weather=="비" or weather=="눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온 : "))
# if 30<= temp:
#     print("쪄죽으니 나가지 마세요")
# elif 10<=temp and temp<30:
#     print("나쁘지 않은 날씨군요")
# elif 0<=temp<10:
#     print("춥군")
# else:
#     print("나가면 죽겄다")

#for문 -----------------------------------------------------------------------
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
#
# for waiting_nom in range(5):
#     print("대기번호 : {0}".format(waiting_nom))
#
# starbucks=["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:
#     print(f"->{customer}님 커피 다됐습니다")

# while문    ------------------------------------------------------------------
# customer="토르"
# index=5
# while index>=1:
#     print(f"{index}번 말하고 버립니다아~ {customer}님 커피가 준비돼었습니다 ")
#     index-=1
#     if index==0:
#         print("커피 버렸습니다^^")
# print("안녕히 가세요~~")

#무한루프
# customer="아이언맨"
# index=1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer,index))
#     index+=1

# customer="토르"
# person="hwo"
# while person !=customer:
#     print(f"{customer}님 커피 다됐삼")
#     person=input("이름이 뭐예요~ \n=")
#     if(person=="토르"):
#         print("네 가져가세요~")
#     else: print("미완성입니다.")

#continue 와 break   -----------------------------------------------------------
# absent =[2,5] #결석
# no_book=[7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"오늘 수업 여기까지. {student}번 따라와")
#         break
#     print(f"{student}번 책읽어~")

#한줄 for문    ---------------------------------------------------------------
#출석번호가 1,2,3,4 앞에 100을 붙이기로 함 ->101 102 103 104
# students=[1,2,3,4,5]
# print(students)
# students=[i+100 for i in students]  #student index가 끝날때까지 students+100해서 집어너어라
# print(students)
#
# #학생 이름을 길이로 변환
# students=["mirim","gijang","dachong"]
# students=[len(i) for i in students]
# print(students)
#
# #학생 이름을 대문자로 변환
# students=["mirim","gijang","dachong"]
# students =[i.upper() for i in students]
# print(students)

#퀴즈 5   ---------------------------------------------------------------------
#나는 cocoa 서비스를 이용하는 택시 기사
#50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램 작성

#조건 1 : 승객별 운행 소요 시간은 5분 ~50분 사이의 난수로 정해집니다
#조건 2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야합니다

# from random import *
# time=0
# cnt=0
# for i in range(1,51):
#     time= randint(5,50)
#     if 5 <= time <= 15 :
#         print("[O] {0}번째 손님 (소요시간 : {1}분 )".format(i,time))
#         cnt+=1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분 )".format(i,time))
#
# print(f"총 탑승 승객 : {cnt} 명")

#함수 --------------------------------------------------------------------------
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_account()
#
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance + money))
#     return balance + money
#
# def withdraw(balance,money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("잔액이 모자랍니다. 잔액은 {}원입니다. ".format(balance))
#         return balance
# def withdraw_night(balance, money):
#     commission = 100 #수수료 100원
#     return commission, balance - money-commission
# balance =0
# balance = deposit(balance, 3000)
# # balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print(f"수수료는 {commission}원이며, 잔액은 {balance}원입니다.")

#기본값    ---------------------------------------------------------------------
# def profile(name, age, main_lang):
#     print(f"이름 : {name} \t나이 : {age}\t주 사용 언어 : {main_lang}")
#
# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

#같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age=17, main_lang="파이썬"):
#     print(f"이름 : {name} \t나이 : {age}\t주 사용 언어 : {main_lang}")
# profile("나미림",17,"자바")
# profile("너미림")
    
#키워드값   ---------------------------------------------------------------------
# def profile(name, age, main_lang):
#      print(name, age, main_lang)
#
# profile(name="유재석",main_lang="파이썬",age=20)
# profile(main_lang="파이썬",age=25,name="김태호")

#가변인자   ---------------------------------------------------------------------
#가변 인자를 사용하지 않았을 때 바껴도 빨리 처리 어려움
# def profile(name, age, lang1, lang2,lang3,lang4):
#     print(f"이름 : {name}\t나이 : {age}\t",end=" ")
#     print(lang1, lang2, lang3, lang4)

#가변인자 사용 시         #들어오는 언어개수에 상관없이 출력시킴 for문
# def profile(name, age, *language):
#     print(f"이름 : {name}\t나이 : {age}\t",end=" ")
#     for lang in language:
#         print(lang, end=" / ")
#
# profile("유재석",20,"python","java","C","C++","javaScript")
# print()
# profile("김태호",25,"Kotlin","Swifft")

#지역 변수와 전역변수 -------------------------------------------------------------
# gun = 10
# def checkpoint(soldiers): # 경계근무
#     global gun
#     gun = gun - soldiers
#     print("[함수 내 ] 남은 총 : {0}".format(gun))
#
# def checkpoint(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내 ] 남은 총 : {0}".format(gun))
#     return gun
#
# print("전체 총 : {0}".format(gun) )
# gun = checkpoint(gun,2)
# print("남은 총 : {0}".format(gun) )

#퀴즈 6   ----------------------------------------------------------------------
#표준 체중을 구하는 프로그램을 작성
# 표준 체중 : 각 개인의 키에 적당한 체중

# 성별에 따른 공식
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)

# def std_weight(height,gender):
#     if gender =="여자" :
#         return height*height*21
#     elif gender == "남자":
#         return height*height*22
#     else :
#         print("성별오류")
#         return 0
# height=175
# gender="남자"
# weight=round(std_weight(height/100,"남자"),2) #반올림 함수
# print("키 {0} cm {1}의 표준 체중은 {2}kg입니다." .format(height,gender,weight))

#표준입출력  --------------------------------------------------------------------
# import sys
# print("Python", "Java", file= sys.stdout)
# print("Python", "Java", file= sys.stderr)

# scores = {"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(4), str(score).rjust(4), sep=":") #왼쪽으로 정렬하는데 8칸을 띄워라 ljust()

#은행 대기순번표
#001,002,003
# for num in range(1,21):
#     print("대기번호 : "+ str(num).zfill(3))

# answer = input("아무값이나 입력하세요 : ")
# answer =10
# print(type(answer))
# print('입력하신값은 '+ answer+'입니다.')

#다양한 출력포맷   ---------------------------------------------------------------
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자기 공간을 확보
# print("{0:>10}".format(500))
# #양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0:>+10}".format(500))
# print("{0:>+10}".format(-500))
# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(-500))
# #3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000000))
# #3자리 마다 콤마를 찍어주기 +-부호도 붙이기
# print("{0:,}".format(100000000000000))
# print("{0:,}".format(-100000000000000))
# #3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# print("{0:^<+30")
# #소수점 출력
# print("{0:f}".format(5/3))
# #소수점 특정 자리수까지만 표시
# print("{0:.2f}".format(5/3))

#파일 입출력 --------------------------------------------------------------------
#score이라는 파일을 생성한다. 생성한뒤 내용을 넣는다.
# score_file = open("score.txt","w",encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

#원래 있던 파일을 가져와서 추가시킨다 줄바꿈이 되지않으므로 \n를 써준다.
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
#
# # 파일의 내용을 읽어온다.
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

#파일의 내용을 한줄씩 읽어오고 커서는 다음 줄로 이동한다.
# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

#한줄씩 출력
# score_file = open("score.txt","r", encoding="utf8")
# lines = score_file.readlines() #리스트 형태로 저장
# for line in lines:
#     print(line, end="")

#줄의 길이를 모를 때 출력
# score_file = open("score.txt","r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

#pickle ----------------------------------------------------------------------
#프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해서 다시 쓸수 있는것
# import pickle
#파일 생성 및 오픈해서 넣기
# profile_file= open("profile.pickle",'wb') #프로필 생성
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile) #출력
# pickle.dump(profile, profile_file) #프로필에 있는 정보를 file에 저장
# profile_file.close()

#파일에서 읽기위해 가져오는 것
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

#with   ------------------------------------------------------------------------
import pickle

#파일을 열어서 읽어와서 profile_file이라는 변수에 저장하고 pickle.load를 이용해서 읽은후 출력
# with open('profile.pickle',"rb") as profile_file : #읽기 바이너리
#     print(pickle.load(profile_file))
#     #with문을 탈출하면서 자동으로 종료해줌 .close()안써도됨

# #파일 쓰기
# with open('study.txt',"w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
#
# #파일 읽기
# with open('study.txt',"r", encoding="utf8") as study_file:
#     print(study_file.read())

#퀴즈 7   ----------------------------------------------------------------------
#당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
#보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성
# 조건 : 파일명은 '1주차.txt' , '2주차.txt' ...와 같이 만든다
#
# for i in range(1,51):
#     with open(str(i)+'주차.txt',"w",encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 - ".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")
#클래스    ------------------------------------------------------------------------
#클래스가 없었을 때
#마린 : 공격 유닛, 군인, 총을 쏠수 있음
# name="마린"
# hp =40
# damage=5
#
# print("{} 유닛이 생성되엇습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))
#
# #탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank2_name="탱크"
# tank2_hp=150
# tank2_damage=35
#
# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))
#
# def attack(name,location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))
#
# attack(name,"1시",damage)
# attack(tank2_name,"1시",tank2_damage)

#클래스 생성
# class Unit:
#     def __init__(self,name,hp,speed): #생성자
#         self.name = name
#         self.hp= hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location,self.speed))

# marine1 = Unit("마린",40)
# marine1 = Unit("마린",40)
# marine1 = Unit("탱크",150)

#멤버 변수 -------------------------------------------------------------------------
#레이스 : 공중 유닛 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스",80,5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#
# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("레이스",80,5)
# wraith2.clocking = True
#
# if wraith2.clocking==True:
#     print("{0} 는 현재클로킹 상태입니다.".format(wraith2.damage))

#메소드    -------------------------------------------------------------------------
#공격 유닛
# class AttackUnit(Unit): #상속 받음
#     def __init__(self,name,hp,damage,speed): #생성자
#         Unit.__init__(self,name,hp,speed)
#         self.damage=damage
#
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")
#
#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입엇습니다.")
#         self.hp -=damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp<=0:
#             print(f"{self.name} :  파괴되었습니다")

# 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

#공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

#다중 상속  -------------------------------------------------------------------
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")
#
# #공중 공격 유닛 클래스
# class FlyableAttackkUnit(AttackUnit, Flyable):
#     def __init__(self, name,hp,damage, flying_speed):
#         AttackUnit.__init__(self, name, hp,damage,0)
#         Flyable.__init__(self, flying_speed)
#
#     #AttackUnit이 상속받은 Unit의 move 메서드를 오버라이드
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackkUnit("발키리", 200,6,5)
# valkyrie.fly(valkyrie.name, "3시")
#
# #벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐",80,10,20)
#
# #배틀크루져 : 공중유닛, 체력도 굉장히 좋음 공격력 좋음
# battlecruiser = FlyableAttackkUnit("배틀크루져",500,25,3)
#
# vulture.move("11시")
# # battlecruiser.fly("9시",battlecruiser.name)
# battlecruiser.move("9시")

#pass   -----------------------------------------------------------------------------------
# #건물
# class BuildngUnit(Unit):
#     def __init__(self, name,hp,location):
#         Unit.__init__(self,name,hp,0)
#         super().__init__(name,hp,0)
#         self.location = location
    
# # 서플라이 디폿 : 건물 , 1개 건물 =8 유닛.
# supply_depot= BuildngUnit("서플라이 디폿",500,"7시")
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     pass
#
# game_start()
# game_over()

#스타크래프트 ---------------------------------------------------------------------
# from random import *
#
# #일반유닛
# class Unit:
#     def __init__(self,name,hp,speed): #생성자
#         self.name = name
#         self.hp= hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
#
#     def move(self, location):
#         print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")
#
#     # 공격 받았을때
#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입엇습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} :  파괴되었습니다")
#
# #공격 유닛
# class AttackUnit(Unit): #상속 받음
#     def __init__(self,name,hp,speed,damage): #생성자
#         Unit.__init__(self,name,hp,speed)
#         self.damage=damage
#
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")
# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self,"마린",40,1,5)
#
#     #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 자기 체력 10 감소
#     def stimpack(self):
#         if self.hp>=10:
#             self.hp-=10
#             print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
#         else:
#             print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")
#
# #탱크
# class Tank(AttackUnit):
#     #시즈 모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     seize_developed = False # 시즈모드 개발여부
#
#     def __init__(self):
#         AttackUnit.__init__(self,"탱크",150,1,35)
#         self.seize_mode=False   #멤버변수 정의
#
#     def set_seize_mode(self):
#         if Tank.seize_developed ==False:
#             return
#         #현재 시즈모드가 아닐때 -> 시즈모드
#         if self.seize_mode ==False:
#             print(f"{self.name} : 시즈모드로 전환합니다.")
#             self.damage *=2
#             self.seize_mode=True
#
#         #현재 시즈모드일 때 -> 시즈모드 해제
#         else :
#             print(f"{self.name} : 시즈모드로 해제합니다.")
#             self.damage /= 2
#             self.seize_mode = False
#
# #날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")
#
# #공중 공격 유닛 클래스
# class FlyableAttackkUnit(AttackUnit, Flyable):
#     def __init__(self, name,hp,damage, flying_speed):
#         AttackUnit.__init__(self, name, hp,0,damage)
#         Flyable.__init__(self, flying_speed)
#
#     #AttackUnit이 상속받은 Unit의 move 메서드를 오버라이드
#     def move(self, location):
#         self.fly(self.name, location)
#
# #레이스
# class Wraith(FlyableAttackkUnit):
#     def __init__(self):
#         FlyableAttackkUnit.__init__(self,"레이스",80,20,5)
#         self.clocked = False #클로킹 모드 해제상태
#
#     def clocking(self):
#         if self.clocked==True :  #클로킹 모드 -> 모드 해제
#             print(f"{self.name} : 클로킹 모드를 해제합니다.")
#             self.clocked = False
#
#         else:   #클로킹 모드 해제 -> 모드 설정
#             print(f"{self.name} : 클로킹 모드를 설정합니다.")
#             self.clocked = True
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다. ")
#
# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")
#
# #실제 게임 진행   -------------------------------------------------------------------
# game_start()
#
# #마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
#
# #탱크 2기 생성
# t1 = Tank()
# t2 = Tank()
#
# #레이스 1기 생성
# w1 = Wraith()
#
# #유닛 일괄 관리 : 리스트를 만들어서 관리 (생성된 모든 유닛 append)-추가
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)
#
# # 전군 이동
# for unit in attack_units :
#     unit.move("1시")
#
# #탱크 시즈모드 개발 : 가는 와중에
# Tank.seize_developed=True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
#
# #공격 모드 준비 ( 마린: 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()
#
# #전군 공격
# for unit in attack_units:
#     unit.attack("1시")
#
# #전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21)) #공격은 랜덤으로 받음(5~20)
#
# # 게임 종료
# game_over()

# 퀴즈 8  -----------------------------------------------------------------------
# 부동산 프로그램 작성
# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#                    #   매물위치    오피스텔 등  전세/매매/월세  가격    중공년도-만든년도
#         self.location= location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#
#     #매물 정보 표시
#     def show_detail(self):
#         print(self.location,self.house_type,self.deal_type,self.price,self.completion_year+"년")
#
#
# h1 = House("강남","아파트","매매","10억","2010")
# h2 = House("마포","오피스텔","전세","5억","2007")
# h3 = House("송파","빌라","월세","500/50","2000")
#
# homes = []
# homes.append(h1)
# homes.append(h2)
# homes.append(h3)
#
# print("총 {0}대의 매물이 있습니다.".format(len(homes)))
# for h in homes:
#     h.show_detail()

# 모듈 --------------------------------------------------
# 함수정의, 클래스 등 파이썬 문장을 담고 있는 파일 = 모듈 (.py)
# 같은 경로에 있어야지만 불러와서 사용가능

# 1. import를 사용해서 모듈 불러오기
# import theater_module
# theater_module.price(3) # 3명이서 영화보러 갔을때
# theater_module.price_morning(4) # 3명이서 영화보러 갔을때
# theater_module.price_soldier(5) # 3명이서 영화보러 갔을때

# import theater_module as mv # 모듈 임포트 시 사용할 별칭을 지정할 수 있다. as
# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(5)

# 2. from 이용해서 모듈의 모든함수 사용하기  - 모듈에 있는 모든걸 사용, 앞에 이름 기제X
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# 3. 필요한 함수만 가져와서 사용하기
# from theater_module import price,price_morning
# price(5)
# price_morning(6)
# price_soldier(7)    # 사용기제 안해서 에러남

# from theater_module import price_soldier as price   # 함수이름에 사용별칭 정의
# price(6)

# 패키지 -----------------------------------------------------------------------
# 하나의 디렉토리에 여러 모듈 파일들을 갖다놓은것 = 모듈들의 집합

# 첫번째 방법 - import - 접근 : 폴더.파일.클래스
# import travel.thailand
# # import travel.thailand.ThalandPackage   # 이런식으로는 사용안됨 에러남
# trip_to = travel.thailand.ThailandPackage() 
# trip_to.detail()

# 두번째 방법    - from - 접근 : 클래스
# from travel.thailand import ThailandPackage # from 으로는 사용가능
# trip_to = ThailandPackage()
# trip_to.detail()

# 세번째 방법 - 폴더에서 파일 꺼내기 - 접근 : 파일.클래스
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__   ----------------------------------------------------
# 패키지 내에서 * 구문(모두참조) 사용 시 참조시킬 파일을 정의하는것
# from random import *
#from travel import *       # 패키지 안에 포함된 것들 중에서 __init__ 파일에서 공개범위를 설정해줘야함
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 모듈 직접 실행   -------------------------------------------------
# 실제로 패키지나 모듈 만들때는 직접 테스트를 해봐야한다.

# 각 파일단위 모듈안에 이런식으로 기재한다.
'''if __name__ == "__main__":  # thailand.py 에서 실행시켯을 때는 이문장이 실행됨
    print("Thailand 모듈을 직접 실행")
    # 이문장은 모듈을 직접 실행할 때만 실행된다
    trip_to = ThailandPackage()
    trip_to.detail()
else:   # 만약 practice에서 thailand.py를 갖다쓸때는 이문장이 실행됨
    print("Thailand 외부에서 모듈 호출")'''


# 패키지 모듈 위치     ---------------------------------------------------
# 모듈이나 패키지를 호출하는 같은 경로에 있어야 참조가 가능하다
# 파일의 위치(경로)를 가져와서 참조가능할수있게 해야함
# import inspect  # 경로를 가져오게하는 도구
# import random   # 경로를 가져올 파일 import
# import travel.thailand
# print(inspect.getfile(random))  # geetfile(파일) 위치를 반환
# print(inspect.getfile(thailand))

