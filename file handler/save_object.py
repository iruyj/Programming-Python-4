# 객체 생성
import pickle

from person import Person
번호15 = Person('이재령','하얀색')
번호17 = Person('임사랑','분홍색')

# 리스트 만들기
절친 = [번호15, 번호17]
print(번호17)
for 친구 in 절친:
    print(친구)
    
# 저장하기
# 1. 객체 하나 저장
with open('object.bin', 'wb') as f:
    # f.write(번호15)  <- 객체쓰기 이렇게 못함
    pickle.dump(번호15, f)

# 2. 객체 여러개 저장
with open('objects.bin', 'wb') as f:
    pickle.dump(절친,f)