# Sequence
# 컨테이너 Container : 서로 다른 자료형 list tuple collections.deque
# 플랫 Flat : 한개의 자료형 str, bytes, bytearray
# mutable : list bytearray array.array memoryview deque
# immutable : tuple str bytes

# Tuple
# unpacking

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*divmod(100, 9))

print()

x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

# mutable vs immutable

m = (15, 20, 25)
n = [15, 20, 25]
print(m, id(m))
print(n, id(n))

m *= 2
n *= 2
print(m, id(m))  # 튜플 id 값 다름
print(n, id(n))  # 리스트 id 값 같음

print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func ...

# sorted 정렬 후 새로운 객체 변환
fruits = ['orange', 'apple', 'watermelon', 'pineapple', 'kiwi']
print('sorted:', sorted(fruits))
print('sorted:', sorted(fruits, reverse=True))
print('sorted:', sorted(fruits, key=len))
print('sorted:', sorted(fruits, key=lambda x: x[-1], reverse=True))
print()
# sort 정렬 후 객체 직접 변경
#  반환값 확인 None
print('sort:', fruits.sort(), fruits)
print('sort:', fruits.sort(reverse=True), fruits)
print('sort:', fruits.sort(key=len), fruits)
print('sort:', fruits.sort(key=lambda x: x[-1], reverse=True), fruits)

# list vs array
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫지 기반 : 배열(리스트와 거의 호환)



