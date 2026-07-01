students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana" : 96
}

print("Student Marks")

for name, mark in students.items():
    print(f"{name}: {mark}")

average = sum(students.values()) / len(students)

print("\nAverage:", average)