# Sequence
# 컨테이너 Container : 서로 다른 자료형 list tuple collections.deque
# 플랫 Flat : 한개의 자료형 str, bytes, bytearray
# mutable : list bytearray array.array memoryview deque
# immutable : tuple str bytes
# hashtable 해시테이블
# key 에 값을 저장하는 구조
# 파이썬 dict 해시 테이블
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조

# Dict 구조
# print(__builtins__.__dict__)

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2))
# mutable 구조는 hash 를 이용할 수 없음

print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'),)

dict1 = {}
dict2 = {}

# no use Setdefault

for k, v in source:
    if k in dict1:
        dict1[k].append(v)
    else:
        dict1[k] = [v]

print(dict1)

# use Setdefault
for k, v in source:
    dict2.setdefault(k, []).append(v)

