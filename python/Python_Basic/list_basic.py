'''
list -> 배열

1. 시퀀스형 -> 순서를 가지고 있다(이어져 있다)
    인덱스 -> 인덱싱, 슬라이싱 -> 인덱스를 이용한 함수 사용이 가능
2. 값 변경이 가능(mutable)
    mutable vs immutable
    mutable - 리스트, 딕셔너리, 셋 값 변경 가능
    immutable - 숫자, 문자, 튜플, 값 변경 불가능
'''

# x = [1, 2]
# y = x

# y.append(3)

# print(x)
# print(y)


x = 1
y = x

y += 1

print(y)
print(x)


'''
얕은 복사 vs 깊은 복사
'''

# 얕은 복사 mutable -> 메모리 참조 -> =, [:], object.copy()
list1 = [1, 2, 3, 4]
list2 = list1

list1.append(5)

print(id(list1))
print(id(list2))

list_ = [3, 4]

list3 = [1, 2, list_]
list4 = [list_, 5]

list4.append(6)

print(id(list3[2:3]))
print(id(list4))

# 깊은 복사 immutable -> 객체 복사 (id값은 같음) -> deepcopy()
num1 = 1
num2 = num1

num2 += 1