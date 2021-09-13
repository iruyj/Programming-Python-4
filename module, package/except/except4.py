list1 = [1,2,3]
try:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
except:
    print('error')
else:   # 예외가 발생하지 않을때 실행한다.
    print('It does work well.')
finally:    # 무조건 마지막에 실행됨
    print('finally')

#-- 한번에 모아서 출력되는데 에러를 먼저 출력시킨다.

