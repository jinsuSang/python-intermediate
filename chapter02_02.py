# 객체 지향 프로그래밍 OOP
# 규모가 큰 프로젝트 -> 함수 중심

# self 는 인스턴스 자신의 고유값을 저장하는 예약어
import time


class Car:
    """
    Car class
    Author: jinsuSang
    Date: 2021.07.17
    """

    # 클래스 변수
    # del 사용시 클래스 변수에 접근하는 것은 좋지 못하다고 생각함
    # 클래스 변수는 read only 형식을 사용하는 것을 개인적으로 추천
    car_count = 0

    def __init__(self, company, details):
        self.__company = company
        self.__details = details
        Car.car_count += 1

    def __del__(self):
        Car.car_count -= 1
        print('delete', self.car_count, Car.car_count)

    def __repr__(self):
        return 'repr: {} {}'.format(self.company, self.details)

    @property
    def company(self):
        return self.__company

    @property
    def details(self):
        return self.__details

    def instance_details(self):
        print('instance id: {}'.format(id(self)))
        print('company = {}, price = {}'.format(self.company, self.details.get('price')))


car1 = Car('KIA', {'color': 'White', 'horsepower': 400, 'price': 4000})
car2 = Car('Tesla', {'color': 'Red', 'horsepower': 600, 'price': 14000})
car3 = Car('Samsung', {'color': 'Blue', 'horsepower': 500, 'price': 5000})
cars = [car1, car2, car3]
# id 확인
for car in cars:
    print(id(car))

print(car1.company == car2.company)
print(car1 is car2)

# dir and __dict__
print(dir(car1))
for car in cars:
    print(car.__dict__)

print()

# Document
print(Car.__doc__)

# instance details
car1.instance_details()
car2.instance_details()

# 비교
print(car1.__class__ == car2.__class__)  # True
print(id(car1.__class__) == id(car2.__class__))  # True, 클래스 id 동일, 인스턴스 id 다름

# 클래스 함수 활용과 클래스 변수
Car.instance_details(car1)
Car.instance_details(car2)
print(Car.car_count)
print(car1.car_count)

# 인스턴스 삭제가 아닌 레퍼런스 주소와의 관계를 끊음
del car2

print(Car.car_count)
print(car1.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 같은 이름으로 변수 생성 가능하고 인스턴스 검색 후 변수 없을 시 클래스에서 검색
