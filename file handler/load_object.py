import pickle

# 객체 하나 불러오기
with open('object.bin', 'rb') as f:
    p1 = pickle.load(f)
print(p1)

# 객체 여러개 가져오기
with open('objects.bin','rb') as f:
    people = pickle.load(f)
# print(people)   # [<person.Person object at 0x0000022517278670>, <person.Person object at 0x00000225172A8940>]
# print(people[0])
# print(people[1])
for person in people:
    print(person)