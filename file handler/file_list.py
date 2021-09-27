#디렉토리의 현재 파일과 디렉토리 리스트 보여주기
import os

#data = os.listdir('c:\\')      # c:\ <- c부터 절대경로
#data = os.listdir('..')      # 현재를 기준으로 상위 디렉토리 (상대경로)
data = os.listdir('.')      #현재 디렉토리를 리스트화 하라는말
data = os.listdir('my_directory')      #현재 디렉토리 기준 하위디렉토리 (상대경로)
for d in data:
    print(d+"---------------")
    print('is directory?: '+str(os.path.isdir(d)))  #디렉토리인지 확인하기
    print('is directory?: '+str(os.path.isfile(d)))  #파일인지 확인하기
