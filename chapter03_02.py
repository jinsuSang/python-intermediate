# 매직 메소드
# 파이썬 핵심
# sequence, iterator, functions, class
# 클래스 안에 정의할 수 있는 특별한  built-in 메소드

# 클래스 예제2
# 벡터 (x, y) (5, 2)

class Vector(object):
    def __init__(self, x=0, y=0):
        """
        Create a vector
        v = Vector(10, 20)
        :param x: real number
        :param y: real number
        """
        self.__x, self.__y = x, y

    def __repr__(self):
        return f'Vector({self.__x}, {self.__y})'

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __mul__(self, other):
        return Vector(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        return Vector(self.__x / other, self.__y / other)

    def __floordiv__(self, other):
        return Vector(self.__x // other, self.__y // other)

    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)

    def __bool__(self):
        return bool(max(self.__x, self.__y))


print(Vector.__init__.__doc__)

v1 = Vector(2, 5)
print(v1)

v2 = Vector(3, 4)
print(v1 + v2)

print(bool(Vector(0, 0)), bool(v2))

v3 = Vector(5, 6)
print(v1 + v2 + v3)
