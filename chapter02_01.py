# 객체 지향 프로그래밍 OOP
# 규모가 큰 프로젝트 -> 함수 중심


# 클래스 구조
# private __ protected _
# __str__ : 사용자 레벨, 간단한 print 사용
# __repr__ : 개발자 레벨, 객체 정보를 제공시 사용
# __str__이 __repr__ 보다 우선
# https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__#3
class Car:
    def __init__(self, company, details):
        self.__company = company
        self.__details = details

    @property
    def company(self):
        return self.__company

    @property
    def details(self):
        return self.__details

    def __repr__(self):
        return 'repr: {} {}'.format(self.company, self.details)


car1 = Car('KIA', {'color': 'White', 'horsepower': 400, 'price': 4000})
car2 = Car('Tesla', {'color': 'Red', 'horsepower': 600, 'price': 14000})
car3 = Car('KIA', {'color': 'Blue', 'horsepower': 500, 'price': 5000})

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()
print()

cars = list()
cars.append(car1)
cars.append(car2)
cars.append(car3)

print(cars)

# repr 명시적 사용
for car in cars:
    print(repr(car))
