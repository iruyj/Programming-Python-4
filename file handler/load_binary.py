with open('binary.bin','rb') as f:
    data = f.read()     # b'\xff\x00\x7f'
print(data)


# 커밋 두개 잡고 오른쪽 마우스 : squash 커밋 누르면 합쳐짐