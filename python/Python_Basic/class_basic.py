'''
Class : 코드를 재사용 -> 함수 모음집

계산기

class : 틀
Instance : 틀로 찍어낸 결과물
Method : 클래스 내부의 함수
'''
result = 0
result2 = 0


def add(number):
    global result
    result += number
    return result

def add2(number):
    global result2
    result2 += number
    return result2

print(add(1))
print(add(2))


# 더하기 클래스
class Add:
    def __init__(self): # __init__ 무조건 실행되는 코드
        self.result = 0 # 인스턴스 변수 result=0일 경우 클래스 변수

    def add(self, number):
        self.result += number
        return self.result
    
# Add로 만든 결과물(객체, 인스턴스)
'''
Add
- 인스턴스
    result = 0
    def add()
'''
add_func = Add()
add_func2 = Add()

add_func2.add(5)

# 클래스의 상속 : 외부에 정의된 기능을 사용하고 싶을 때
# class Sub
# class Add(Sub)
# sub2

# 메소드 오버라이딩 : 상속받아온 기능을 재정의해서 쓸 때