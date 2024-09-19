def average_grade(records):
    total_grade = sum(record[2] for record in records)
    return total_grade/ len(records)
student = (
    ("james",20,85)
    ("sumeet",22,90)
    ("modi",21,44)
)
def main():
    avg_grades = average_grade(student)
    print("average Grades",avg_grades)
    