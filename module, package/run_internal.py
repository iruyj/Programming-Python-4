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
import math
fee = 59827
print((math.floor(fee/100))*100)

# 2번 : 100점만점
score = 93
print(round(score,-1))
score = 56
print(round(score,-1))

# 3번 로또 복권 자동생성기
import random
lotto = [random.randint(1,45+1) for _ in range(6+1)]
print(lotto)

# 4번 : 1~9 중복되지 않는 숫자 세자리
nums =random.sample(range(1,9+1),3)
for num in nums:
    print(num,end="")
    
# 5번 : 내가 태어난 날로부터 지난 날
import datetime
now = datetime.datetime.now()
birth = datetime.datetime(2004,8,10)
print((now-birth).days,"일")

# 6번 : 올해 크리스마스까지 며칠 남았는지
now = datetime.datetime.now()
crismas = datetime.datetime(2021,12,25)
print((crismas-now).days,"일")

# 7번 : 내 생일이 얼마나 남았는지
now = datetime.datetime.now()
birth = datetime.datetime(2022,8,10)
print((birth-now).days,"일")

# 8번 : 랜덤하게 번호로 자리를 배치하는 방법
def randomPlace(lines,nums,*exceptnums):
    nums = list(range(1, nums+1))
    for en in exceptnums:
        nums.remove(en)
    random.shuffle(nums)
    cnt =0
    for num in nums:
        print(num,end="\t")
        cnt+=1
        if cnt>=lines:
            cnt=0
            print()

randomPlace(4,18,3)
