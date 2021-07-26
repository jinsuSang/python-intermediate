# Sequence
# 컨테이너 Container : 서로 다른 자료형 list tuple collections.deque
# 플랫 Flat : 한개의 자료형 str, bytes, bytearray
# mutable : list bytearray array.array memoryview deque
# immutable : tuple str bytes

# list comprehending
chars = '+_)(*&^%$#@!~'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending lists + map, filter
code_list3 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list3)

print([chr(x) for x in code_list1])
print([chr(x) for x in code_list3])

# Generator 생성
# https://docs.python.org/ko/3/library/array.html
import array

# Generator 한 번에 한 개의 항목을 생성하고 메모리를 유지하지 않는다
t1 = (ord(s) for s in chars)
print(type(t1))
print(next(t1))


arr1 = array.array('I', (ord(s) for s in chars))
print(type(arr1))
print(arr1.tolist())


print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

# 리스트 주의
marks1 = [['~'] * 2 for n in range(3)]
print(marks1)
marks2 = [['~'] * 2] * 3
print(marks2)

# 수정
marks1[0][1] = 'X'
print(marks1)
# [['~', 'X'], ['~', '~'], ['~', '~']]

marks2[0][1] = 'X'
print(marks2)
# [['~', 'X'], ['~', 'X'], ['~', 'X']]

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])