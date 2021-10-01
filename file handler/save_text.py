# 파일을 실제로 열기
f = open('text.txt', 'w', encoding='utf-8')

f.write('전유리 ')
f.write('남색\n')
f.write('이유빈\n')
f.write('초록색')

f.close()  # 닫기

with open('text.txt','w',encoding='utf-8') as f:
    f.write('전유리 ')
    f.write('남색\n')
    f.write('이유빈\n')
    f.write('초록색')
# with는 close가 없어도 된다 바로 가져와서 넣어줌
