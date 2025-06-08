class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, My name is {self.name}. And I am {self.age} years old.")

# 객체 생성
person1 = Person("John", 36)
person2 = Person("Alice", 20)

# 매서드 호출
person1.greet()     # Hello, My name is John. And I am 36 years old.
person2.greet()     # Hello, My name is Alice. And I am 20 years old.