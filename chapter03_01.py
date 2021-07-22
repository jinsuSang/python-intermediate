# 매직 메소드
# 파이썬 핵심
# sequence, iterator, functions, class
# 클래스 안에 정의할 수 있는 특별한  built-in 메소드

print(int)
print(float)

print(dir(int))
print(dir(float))

n = 10
print(n + 1000)
print(n.__add__(1000))
# print(n.__doc__)

print(n.__bool__(), bool(n))
print(n.__mul__(100))


# 클래스 예제
class Fruit:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return 'Fruit Class Info : {} {}'.format(self.__name, self.__price)

    def __add__(self, other):
        return self.__price + other.__price

    def __sub__(self, other):
        return self.__price - other.__price

    def __le__(self, other):
        return self.__price <= other.__price

    def __lt__(self, other):
        return self.__price < other.__price

    def __ge__(self, other):
        return self.__price >= other.__price

    def __gt__(self, other):
        return self.__price > other.__price

    def __eq__(self, other):
        return self.__price == other.__price

    def __ne__(self, other):
        return self.__price != other.__price


orange = Fruit('orange', 1000)
apple = Fruit('apple', 3000)

print(orange + apple)
# 4000
print(orange - apple)
# -2000
print(orange >= apple)
print(orange <= apple)
# False
# True

print(orange)
print(apple)
# Fruit Class Info : orange 1000
# Fruit Class Info : apple 3000

print(orange == apple)
print(orange != apple)
# False
