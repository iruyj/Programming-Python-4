# 파일을 실제로 열기
f = open('text.txt','w', encoding='utf-8')

f.write('나 ')
f.write('옥색\n')
f.write('남\n')
f.write('남색')

f.close()   #닫기
