class Person:
    def greeting(self):
        print("나는 생각한다.")
        
class Student(Person):
    def greeting(self):
        print("나는 공부한다.")
        super().greeting()
        
# tom = Person()
# tom.greeting()

jerry = Student()
jerry.greeting()