class Student():
    name= ""
    age= ""
    fav_color= ""
    grade= "" 
    teacher= ""
    #creating the constructor
    def __init__(self):
        print ("Making a new student...")
    def change_details(self):
        self.name= input("Enter your name: ")
        self.age= input("Enter your age: ")
        self.fav_color= input("Enter your favorite color: ")
        self.grade= input("Enter your grade: ")
        self.teacher= input("Enter your teacher's name: ")
    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.fav_color)
        print(self.grade)
        print(self.teacher)
#creating the object
person= Student()
person.change_details()
person.show_details()
