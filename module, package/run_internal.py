#math
# import math
# print(math.ceil(3.5))
# print(math.floor(3.5))
# print(math.pow(2,10))
# print(math.sin(math.pi/2))

#random
# import random
# import  random
# print(random.random())      # 0.0 ~ 1.0 미만
# print(random.randrange(1,10))   # 1~ 10 미만
# print(random.randint(1,10))     # 1 ~ 10 이하
# list1 = ['굶었음','피자','김치찜']
# print(random.choice(list1))     # 리스트에서 하나 뽑기
#
# print(list1)
# print(random.shuffle(list1))    # 리스트 섞기
# print(list1)
# print(random.sample(list1,2))   # 리스트 2개 뽑기

# #datetime
# import datetime
# print('-'*20)
# now = datetime.datetime.now()
# print(now)
# print(now.day)
# print(now.hour)
# birth = datetime.datetime(2004,8,10,2,30)
# print(birth)
# print(now-birth)

#  퀴즈 ------------------------------------------------------
# 1번 : 100원 미만 절사
# print('1. ------------------')
# import math
# fee = 59827
# print(((fee//100))*100,"원")     #1번방법
# print(fee-fee%100)              #2번
# print(math.floor(fee/100)*100)  #3번
# print((int(fee/100))*100)       #4번
#
# # 2번 : 100점만점
# print('2. -----------------')
# score = 93
# print(round(score,-1))
# print(round(score/10)*10)
#
# # 3번 로또 복권 자동생성기
# print('3. ---------------')
# import random
# lotto = [random.randint(1,45+1) for _ in range(6+1)]
# print(lotto)
# print(random.sample(range(1,45+1),6))
#
#
# # 4번 : 1~9 중복되지 않는 숫자 세자리
# print('4. ---------------')
# nums =random.sample(range(1,9+1),3)
# for num in nums:
#     print(num,end="")
# print()
#
# print(''.join(str(n) for n in nums))       # 조인은 문자로 된 리스트를 이어서 붙여준다.
# print(''.join(map(str,nums)))       # map은 앞에 쓴 형태로 리스트를 모두 변환한다
#
# # 5번 : 내가 태어난 날로부터 지난 날
# print('5. ------------------')
# import datetime
# now = datetime.datetime.now()
# birth = datetime.datetime(2004,8,10)
# print((now-birth).days,"일")
#
# # 6번 : 올해 크리스마스까지 며칠 남았는지
# print('6. -------------------')
# now = datetime.datetime.now()
# crismas = datetime.datetime(2021,12,25)
# print((crismas-now).days,"일")
#
# # 7번 : 내 생일이 얼마나 남았는지
# print('7. -------------------')
# now = datetime.datetime.now()
# mybirth = datetime.datetime(2022,8,10)
# if mybirth< now:    # 생일이 지낫으면
#     mybirth= mybirth.replace(year=2022)
# print((mybirth - now).days, "일")
#
#
import random
# 8번 : 랜덤하게 번호로 자리를 배치하는 방법
def randomPlace(lines,nums,*exceptnums): # 없는사람 가변인수로 받기
    nums = list(range(1, nums+1))   # 1번부터 끝번 리스트 넣기
    for en in exceptnums:   # 없는 번호 제거
        nums.remove(en)
    random.shuffle(nums)    # 자리 랜덤섞기
    cnt =0
    print('----------[ 교탁 ]------------')
    for num in nums:
        print(num,end="\t|\t")
        cnt+=1  # 현재 출력열인덱스
        if cnt>=lines:  # 열 개수마다 들여쓰기한다
            cnt=0
            print()
randomPlace(4,19,3)     # 자리 앉을때 열 개수, 마지막번호, 없는번호들

# 8번 : 수업 풀이
# 재적(전출, 자퇴) 인원 X
import random
# 마지막 번호 묻기
print('\n8번 문제 풀이 -----------------------')
last_num = input('마지막 번호 : ')
# 1~마지막 번호까지 숫자리스트 만들기
class_nums = list(range(1,int(last_num)+1))
print(class_nums)
# 반복
while(True):
    # 제외할 번호 묻기
    except_num = input('제외할 번호 : ')
    # 다뺐으면 끝내기
    if except_num == '':
        break
    # 없는 번호 입력한 경우
    if int(except_num) not in class_nums:
        print('잘못입력했습니다 다시입력하세요')
        continue
    class_nums.remove(int(except_num))  # 리스트에서 빼기
# 리스트 섞기
random.shuffle(class_nums)
# 출력하기
print('자리번호  |  학생번호')
for i,n in enumerate(class_nums):
    print(f'{i}\t\t|\t\t{n}')







