# concurrency 병행성 : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 해결
# parallelism 병렬성 : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')


temp = iter(generator_ex1())

# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in temp:
    print(v)

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)
for i in temp3:
    print(i)

print()
print()

# filterfalse, takewhile, accumulate, chain, product, groupby

import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# 1
# 3.5
# 6.0
# 8.5
# 무한

# 조건

gen2 = itertools.takewhile(lambda n: n < 10, itertools.count(1, 2.5))

for v in gen2:
    print(v)
# 1
# 3.5
# 6.0
# 8.5
# 11.0
# 13.5
# 16.0.

print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [i for i in range(1, 11)])

for v in gen3:
    print(v)

gen10 = itertools.filterfalse(lambda n: n % 2, [i for i in range(1, 11)])

for v in gen10:
    print(v)

print()

gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)
# 1
# 3
# 6
# 10
# 15
# 21
# 28

gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))
# ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]

gen7 = itertools.product('ABCDE')
print(list(gen7))
# [('A',), ('B',), ('C',), ('D',), ('E',)]

gen8 = itertools.product('ABC', repeat=2)
# 경우의 수
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
print(list(gen8))

gen9 = itertools.groupby('AABBCCDDEEEE')
for char, group in gen9:
    print(f'{char} : {list(group)}')

# A : ['A', 'A']
# B : ['B', 'B']
# C : ['C', 'C']
# D : ['D', 'D']
# E : ['E', 'E', 'E', 'E']
