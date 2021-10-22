# 정답 만들기 : 랜덤으로 (0~9까지)
import random
from custom_error import InvalidLengthError

def make_answer():
    answer_nums = random.sample(range(0, 9 + 1), 3)
    return ''.join(str(a) for a in answer_nums)


answer = make_answer()
#print(answer)


# 맞은 개수 체크 함수
def check(guess, answer):
    strike = 0
    ball = 0
    for i, an in enumerate(answer):
        if guess[i] == answer[i]:   #스트라이크 확인하기
            strike += 1
        elif guess.find(an) != -1:    # 볼 확인하기
            ball += 1
    return strike, ball

if __name__ == '__main__':
    cnt = 0
    # 인덱스 에러표시ㅇ
    while True:
        guess = input('맞춰라!! >> ')  # 숫자 묻기
        try:
            guess_int = int(guess)
        except ValueError as e:
            print('숫자를 입력하세요')
            continue
        if len(guess) != len(answer):
            raise InvalidLengthError(f'입력하신 답이 정답의 길이와 다릅니다. {len(answer)}글자')
            # raise = throw 에러로 보내는거

        strike, ball = check(guess, answer)  # strike, ball 판정
        print(f'{guess}\tstrike : {strike}, ball : {ball}')  # 출력하기
        if answer == guess:  # 정답 == 숫자 면 끝내기
            print('>>>>>>>>> 정답이다 하하 <<<<<<<<<<')
            break