# 일급 함수 혹은 일급 객체
# Closure 기초

# 파이썬 scope
b = 5


def func_v1(a):
    global b
    print(a)
    # 10
    print(b)
    # 5
    b = 100
    print(b)
    # 100


print('*****', b)  # 5
func_v1(10)
print('*****', b)  # 100


# Closure 사용 이유
# 서버 프로그래밍 -> 동시성 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착 상태  (데드 락)
# 메모리를 공유하지 않고 메시지 전달로 처리 -> Erlang
# 메시지 전달을 위해 파이썬 클로저는 공유하지만 변경하지 않는 Immutable, READ ONLY 적극 사용 -> 함수형 프로그래밍
# 클로저는 불변자료 구조 및 atom, STM -> 멀티스레드 프로그래밍 강점  coroutine

class Averager():
    def __init__(self):
        self.__series = []

    # 함수로 호출 가능
    def __call__(self, *args):
        self.__series.extend(args)
        print(f'inner => {self.__series} / {len(self.__series)}')
        return sum(self.__series) / len(self.__series)


averager_cls = Averager()
print(averager_cls(10))
# inner => [10] / 1
# 10.0

print(averager_cls(20))
print(averager_cls(30, 40, 50))