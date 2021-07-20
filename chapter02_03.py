# 클래스 기반 메소드 심화

class Car:
    """
    Car class
    Author: jinsuSang
    Date: 2021.07.17
    """

    # 클래스 변수
    # del 사용시 클래스 변수에 접근하는 것은 좋지 못하다고 생각함
    # 클래스 변수는 read only 형식을 사용하는 것을 개인적으로 추천
    __price_per_raise = 1.0

    def __init__(self, company, details):
        self.__company = company
        self.__details = details
        self.__secret = 'secret'

    def __repr__(self):
        return 'repr: {} {}'.format(self.company, self.details)

    # static method, class method 차이
    # https://hamait.tistory.com/635
    # 클래스 메소드
    @classmethod
    def set_per(cls, per):
        if per < 1:
            print('greater than or equal to 1')
            return
        cls.__price_per_raise = per
        print('change per')

    @staticmethod
    def is_tesla(inst):
        if inst.__company == 'tesla':
            return True
        else:
            return False

    @property
    def company(self):
        return self.__company

    @property
    def details(self):
        return self.__details

    # 인스턴스 메소드
    # self: 객체의 고유한 속성값
    def instance_details(self):
        print('instance id: {}'.format(id(self)))
        print('company = {}, price = {}'.format(self.company, self.details.get('price')))

    def get_price(self):
        return self.details.get('price') * Car.__price_per_raise


car1 = Car('kia', {'color': 'White', 'horsepower': 400, 'price': 4000})
car2 = Car('tesla', {'color': 'Red', 'horsepower': 600, 'price': 14000})

car1.instance_details()
car2.instance_details()

print(car1.get_price())
Car.set_per(5)

print(car1.get_price())

print(car1.is_tesla(car1))
print(Car.is_tesla(car1))
