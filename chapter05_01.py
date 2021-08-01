# 일급 함수 혹은 객체
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# factorial
def factorial(n):
    """
    factorial function
    :param n: int
    :return result: int
    """

    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(type(factorial), type(A))
# <class 'function'> <class 'type'>
print(dir(factorial))
print(sorted(set(dir(factorial)).difference(set(dir(A)))))
# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__',
# '__kwdefaults__', '__name__', '__qualname__']

print(factorial.__name__)
# factorial
print(factorial.__code__)
# <code object factorial at 0x000002735C470710, file "C:\Users\sangjs\PycharmProjects\python_intermediate\chapter05_01.py", line 9>

var_func = factorial
print(var_func)
# <function factorial at 0x00000249EF70EEE0>
print(var_func(5))
print(list(map(var_func, range(1, 10))))
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수 higher-order function
# map, filter, reduce
print([var_func(i) for i in range(1, 6) if i % 2])
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))

from dis import dis

dis('[var_func(i) for i in range(1, 6) if i % 2]')
print('--------------------------------')
dis('list(map(var_func, filter(lambda x: x % 2, range(1, 6))))')

# reduce
from functools import reduce
from operator import add

print(sum(range(1, 11)))
print(reduce(add, range(1, 11)))

# 익명함수 lambda
# 가급적으로 주석 작성 필요
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장
print(reduce(lambda x, t: x + t, range(1, 11)))

# callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(factorial))
print(callable(A))


# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5)
print(five(2))
# 10

six = partial(five, 6)
print(six())
# 30

print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))
