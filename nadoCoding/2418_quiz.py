#3-1.------------------------------------------------------------------------------------------------------------
# 주민등록번호 앞 6자리를 변수 id_number에 넣고,
#출생년도 끝 두자리\n출생 월일\n그 두개의 합 출력
# id_number= "040810"
#
# print(id_number[:2])
# print(id_number[-4:])
# print(int(id_number[:2])+int(id_number[2:]))
#
# print('\n===========\n')
#
# #3-2. ------------------------------------------------------------------------------------------------------
# 집 전화번호를 phone_number에 넣고,
# #지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# phone_number="051-0810-2418"
#
# print(phone_number[:phone_number.index("-")])
# print(phone_number[-4:])
#
# phone_number1='010-2540-5357'
# phone_number2='010 7584 1367'
# phone_number3='01012345678'
# # 바꾸는 거 : replace('바꿔야하는문자','바꿀문자')
# result = phone_number1.replace('-', '').replace(' ','')
# print(result)
# print(result)

# Quiz2-1. --------------------------------------------------------------------------------------------------------
# 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

# [풀이]
# student_number = "2100"
# department = int(student_number[1])
# if department==1 or department==2 : print(f"{department}반 뉴미디어소프트웨어과")
# elif department==3 or department==4 : print(f"{department}반 뉴미디어웹솔루션과")
# elif department==5 or department==6 : print(f"{department}반 뉴미디어디자인과")
# else: print("잘못입력했습니다.")

# [다른풀이]
# major=['솦과','웹솔','디자인',]
# number = int(student_number[1])
# if 1<= number <=6:
#     print(f"{number}반 {major[number-1/2]}")
# else:
#     print('잘못입력했습니다.')

# Quiz2-2. ------------------------------------------------------------------------------------------------------------
# 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2

# def get_major(student_number):
#     majors = ['솦','솦','웹','웹','디','디']
#     grade = student_number[0]
#     classroom = int(student_number[1])
#     return grade, majors[classroom-1]
#
# grade, major = get_major('2100')
# print(str(major), grade) #뉴미디어소프트웨어과 2

# [풀이]
# def get_major(argument):
#     department = int(argument[1])
#     if department == 1 or department == 2: return argument[0],"뉴미디어소프트웨어과"
#     elif department == 3 or department == 4: return argument[0],"뉴미디어웹솔루션과"
#     elif department == 5 or department == 6: return argument[0],"뉴미디어디자인과"
# grade, major = get_major('2100')
# print(major,grade)


# Quiz2-3. -------------------------------------------------------------------------------------------------------------
# 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

# [풀이]
# def average(*num):
#     sum=0
#     for n in num:
#         sum+=n
#     return sum/len(num)

    #다른풀이
#     return sum(num)/len(num)
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

# Quiz2-4. -------------------------------------------------------------------------------------------------------------
# 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만
# bmi = get_bmi(176, 69)
# print(bmi) #22.3

# [풀이]
# def get_bmi(cm,kg):
#     return round(kg/(cm/100)**2,1)
#
# bmi= get_bmi(176,69)
# print(bmi)
#
# if bmi>=25: print('비만')
# elif 23<=bmi<25 : print('과체중')
# elif 18.5<=bmi<23 : print('정상')
# elif bmi < 18.5: print('저체중')

# 구구단 출력하기-----------------------------------------------------------------------------
# #구구단 2~7단만 출력
# for i in range(2,9+1):      #2~9
#     print(f'|---{i}단---|')
#     for j in range(1,9+1):  # 1~9
#         print("{0} x {1} = {2}".format(i,j,i*j))
#     if i == 7: break        #7단까지 끝내고 나가기
#
# #구구단 2~7단만 출력 / x(1,3,5,7,9) 인 것만 출력
# for i in range(2,9+1):      #2~9
#     print(f'|---{i}단---|')
#     for j in range(1,9+1):  # 1~9
#         if j%2==0: continue #짝수면 건너뛰기
#         print("{0} x {1} = {2}".format(i,j,i*j))
#     if i == 7: break        #7단까지 끝내고 나가기
#
# Quiz3-1.   -----------------------------------------------------------------------------------
# n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면,
# 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''
result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1

'''

# def n_sum(argument):
#     num = str(argument)
#     if len(num)>=10: return -1
#     elif 10>argument: return argument
#
#     sum = 0
#     for n in range(0,len(num)):
#       sum+=int(num[n])
#     return sum
#
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1


# Quiz3-2.   ------------------------------------------------------------------------------------
# get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''
fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(61)
print(fare)        #1720

'''
# import math  #올림 함수 때문에 사용
# def get_subway_fare(km):
#     fee=720
#     if km>=50:
#         #50 이상이기때문에 10km를 뺀 40km까지는 5km당 100씩, 50km를 초과한 나머지는 올림해서 8km당 100원씩
#         fee+=(40/5*100)+(math.ceil((km-50)/8)*100)
#     elif 10<=km<=50 :
#         #10km이상 50km이하라서 10km를 뺀 뒤 5km당 올림해서 100원씩
#         fee+= (math.ceil((km)/5)*100)
#     return int(fee)
#
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

# Quiz3-3.    ------------------------------------------------------------------------------------
# get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# 힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
'''
result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝

'''
# def get_three_six_nine(num):
#     num=str(num)
#     cnt = num.count('3')+num.count('6')+num.count('9')
#
#     if cnt==0 : return num
#     else : return cnt*'쫙'
#
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝

# Quiz3-4.    ----------------------------------------------------------------------------------
#  나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
# 1. 함수의 이름을 정해준다.
# 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
# 3. 리턴하는 것을 말해준다.
# 4. 출력 예시를 보여준다.
# 5. 내가 낸 문제의 답안을 제출한다.
'''
전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.
cnt_pageNum() 함수에 인수(num)로 전체 페이지 수를 넣고 1페이지에서 끝페이지까지에서
0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 구분해 list를 리턴한다.
매개변수 num<=1000000000

출력 예시
print(cnt_pageNum(11))  #[1, 4, 1, 1, 1, 1, 1, 1, 1, 1]
print(cnt_pageNum(316))  # [61, 169, 162, 79, 62, 62, 62, 61, 61, 61]
print(cnt_pageNum(50))  # [5, 15, 15, 15, 15, 6, 5, 5, 5, 5]
'''
# #[답/풀이]
# def cnt_pageNum(num):
#     one_nine=[0,0,0,0,0,0,0,0,0,0]
#     for n in range(1,num+1):
#         n=str(n)
#         for i in range(10):
#             one_nine[i]+=n.count(str(i))
#     return one_nine
#
# print(cnt_pageNum(11))  #[1, 4, 1, 1, 1, 1, 1, 1, 1, 1]
# print(cnt_pageNum(316))  # [61, 169, 162, 79, 62, 62, 62, 61, 61, 61]
# print(cnt_pageNum(50))  # [5, 15, 15, 15, 15, 6, 5, 5, 5]

# 4-1   --------------------------------------------------------------------------------
'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''
# def is_prime(num):
#     for x in range(2,num):
#         if num%x==0:
#             return "소수 아님"
#     return "소수"

# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님

# 4-2   -------------------------------------------------------------------------------------
'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''
# def get_compliment(str):
#     if str.find("고구마") !=-1 : return "왓쇼이!"
#     elif str.find("맛있는") !=-1 : return "우마이!"
#     elif str.find("놀랄 만한")!=-1 or str.find("황당한")!=-1 or str.find("굉장한")!=-1: return "요모야..!"
#     return "으무!"
#
# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!

# 모듈 Quiz ----------------------------------------------------------
# Quiz5-1. 모듈이란?
#   함수정의, 클래스 등 파이썬 문장을 담고 있는 파일을 말하며 확장자는 .py이다

# Quiz5-2. 패키지란?
#   하나의 디렉토리에 여러 모듈 파일들을 갖다놓은것 = 모듈들의 집합이다


# Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
#   from theater_module import price as p2418
#   p2418(5)

# Quiz5-4. __all__의 역할은?
#   패키지 내에서 * 구문(모두참조) 사용 시 참조시킬 파일을 정의하는 역할이다.
#
# Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
#   if __name__ == "__main__":
#         pass
#   else:
#         pass

# Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 VietnamPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
# import travel.vietnam
# < 가 >
# trip_to = travel.vietnam.VietnamPackage()
# trip_to.detail()

# from travel import vietnam
# < 나 >
# trip_to = VietnamPackage()
# trip_to.detail()

# from travel.vietnam import VietnamPackage
# < 다 >
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()