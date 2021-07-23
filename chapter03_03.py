# 매직 메소드
# 파이썬 핵심
# sequence, iterator, functions, class
# 클래스 안에 정의할 수 있는 특별한  built-in 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

length1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(length1)

# 네임드 튜플

from collections import namedtuple

Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3[0], pt3.x)

length2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(length2)

# namedtuple 선언 방법
Point1 = namedtuple('Point1', ['x', 'y'])
Point2 = namedtuple('Point2', 'x, y')
Point3 = namedtuple('Point3', 'x y')
Point4 = namedtuple('Point4', 'x y x class', rename=True)
# 중복 키나 예약어 사용시 에러가 발생한다.
# 하지만 rename 을 True 로 하면 사용 가능하다.
# rename default value is False
print(Point4)

# dictionary to unpacking
d = {'x': 75, 'y': 650}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(10, 35)
p3 = Point3(15, y=55)
p4 = Point4(10, 20, 30, 40)
# Point4(x=10, y=20, _2=30, _3=40)
# 난수로 키워드 생성
print(p1, p2, p3, p4)

p5 = Point1(**d)
print(p5)

# unpacking
x, y = p2
print(x, y)

# namedtuple method
temp = [25, 36]
# _make(): 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)
p4 = Point1._make((35, 40))
print(p4)

# _fields  : 필드 네임 확인, 키 값 조회
print(p4._fields)

# _asdict() : OrderedDict 반환
print(p4._asdict())

# 실 사용 실습
# 반 30명, 반 4개 (A, B, C, D)

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# list Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(students)

#추천
students2 = [Classes(rank, number)
             for rank in ranks
                 for number in numbers
             ]

print(students2)

for student in students2:
    print(student)