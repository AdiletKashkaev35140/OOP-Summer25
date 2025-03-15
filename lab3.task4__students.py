students = [
    {
        'first_name': 'Adilet',
        'last_name': 'Kashkaev',
        'index_number': '35140',
        'nationality': 'Kyrgyz',
        'starting_date': '2025-03-13',
        'courses': ['Mathematics', 'Computer Science', 'Physics']
    },
    {
        'first_name': 'Elena',
        'last_name': 'Ivanova',
        'index_number': '35141',
        'nationality': 'Russian',
        'starting_date': '2025-03-13',
        'courses': ['Biology', 'Chemistry', 'Mathematics']
    },
    {
        'first_name': 'Omar',
        'last_name': 'Hussein',
        'index_number': '35142',
        'nationality': 'Egyptian',
        'starting_date': '2025-03-13',
        'courses': ['History', 'Physics', 'Computer Science']
    }
]

def add_student(first_name, last_name, index_number, nationality, starting_date, courses):
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'index_number': index_number,
        'nationality': nationality,
        'starting_date': starting_date,
        'courses': courses
    }
    students.append(student)
    print(f"Student {first_name} {last_name} added successfully!")

def display_students():
    for student in students:
        print(f"First Name: {student['first_name']}, Index Number: {student['index_number']}")

if __name__ == "__main__":
    display_students()
    add_student('John', 'Doe', '35143', 'American', '2025-03-13', ['Philosophy', 'Economics'])
    display_students()
