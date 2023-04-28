class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False
    
    def study(self):
        print(f"{self.name} 학생은 공부 중입니다")

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f"{student_1.major}로 전공이 변경되었습니다")

student_1 = Student("현종혁", "컴퓨터공학과")

# 상속(Inheritance) : 부모 클래스의 속성 중 일부 사용, 일부 추가 가능
class ForeignStudent(Student):
    def __init__(self, name, major, country):
        super().__init__(name, major)
        self.country = country
    # 오버라이딩 : 부모 클래스의 내용을 덮어씀
    def study(self):
        print(f"{self.name} is studying right now")
    

