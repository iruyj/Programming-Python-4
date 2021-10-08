with open('binary_to_text.bin', 'wb') as f:
    ga = b'\xea\xb0\x80'    # '가'의 바이너리 코드
    f.write(ga)

with open('binary_to_text.bin','r', encoding='utf-8') as f:
    data = f.read()     #파일 전체를 읽어옴
