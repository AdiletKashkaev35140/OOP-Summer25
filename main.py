class Student:
    def __init__(self, first_name, last_name, index_number, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.index_number = index_number
        self.nationality = nationality

    def display(self):
        return f"Name: {self.first_name} {self.last_name}, Index Number: {self.index_number}, Nationality: {self.nationality}"

students = [
    Student("John", "Doe", "312345", "American"),
    Student("Anna", "Smith", "567890", "British"),
    Student("Ahmed", "Khan", "511223", "Pakistani")
]

for student in students:
    print(student.display())
