print('전체 한꺼번에 읽기')
f = open('text.txt', 'r', encoding='utf-8')  # utf-8 : 읽는것과 쓰는것의 형식이 같아야함
data = f.read()
f.close()

print(data)
print('한줄 씩 읽기')
f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()  # line: 나 옥색\n
    if line == '' :     #끝나는 지점 == 빈칸
        break
    print(line.rstrip())  # 글옆의 빈칸 탭,\n 등이 지워짐
f.close()

print('전체을 한꺼번에 읽고, 줄 별로 리스트')
f = open('text.txt','r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print(line.rstrip())

#퀴즈
f = open('text.txt','r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    datas = line.split(':')
    print('이름:'+datas[0].rstrip()+"\t좋아하는 색 : "+datas[1].rstrip())
