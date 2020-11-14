import collections
import bisect
# Remember the list needs to be sorted for it to work!
Student = collections.namedtuple('Student', ('name', 'grade_point_average'))
Student2 = Student('Jonathan', 3.6)

Student1 = Student('Carly', 3.5)
#print(Student2)
Student3 = Student('John', 3.9)
def comp_gpa(student):
    return (student.name, student.grade_point_average)

def search_student(students, target):
    i = bisect.bisect_left(students, target)
    print(target)
    print(i)
    return 0 <= i < len(students) and students[i] == target

#print(Student2)
print(search_student([Student1, Student2, Student3], Student3))