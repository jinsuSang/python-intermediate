# 일급 함수
# 클로저 기초
# Decorator
# 장점
# 1. 중복제거
# 2. 코드 간결
# 3. 공통 함수 작성
# 4. 로깅, 프레임워크 유효성 체크 -> 공통 기능
# 조합해서 사용 용이

# 단점
# 1. 가독성
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성이 유리
# 3. 디버깅
import time
from operator import add, mul
from functools import reduce


def time_checker(func):
    def time_checked(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()

        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        print('[%0.5fs] %s(%s) => %r' % (end - start, name, arg_str, result))
        return result

    return time_checked


def func1(n):
    return reduce(mul, range(1, n))


def func2(n):
    return reduce(add, range(1, n))


none_deco1 = time_checker(func1)
none_deco2 = time_checker(func2)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

none_deco1(1000)
none_deco2(1000)

print('=' * 15)


@time_checker
def func3(n):
    return reduce(mul, range(1, n))


@time_checker
def func4(n):
    return reduce(add, range(1, n))


func3(1000)
func4(1000)
