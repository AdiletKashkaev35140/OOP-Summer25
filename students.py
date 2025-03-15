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

for student in students:
    print(f"First Name: {student['first_name']}, Index Number: {student['index_number']}")
