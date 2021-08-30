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

#datetime
import datetime
print('-'*20)
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.hour)
birth = datetime.datetime(2004,8,10,2,30)
print(birth)
print(now-birth)