class Student:
    """ Класс студент"""

    def __init__(self, name, surname, gender=''):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def _average(self):
        n = 0
        count = 0
        for keys, value in self.grades.items():
            count += 1
            n += value[0]
        srednee = n / count
        self.average = srednee
        return srednee

    def __str__(self):
        return f"\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {self._average()} " \
               f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} " \
               f"\nЗавершенные курсы:{', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if self.average < other.average:
            print(f"{other.name} {other.surname}")
        else:
            print(f"{self.name} {self.surname}")


class Mentor:
    """Класс преподавателей"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average = 0

    def _average(self):
        n = 0
        count = 0
        for keys, value in self.grades.items():
            count += 1
            n += value[0]
        srednee = n / count
        self.average = srednee
        return srednee

    def __str__(self):
        return f"\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average()}"

    def __lt__(self, other):
        if self.average < other.average:
            print(f"{other.name} {other.surname}")
        else:
            print(f"{self.name} {self.surname}")


class Lecture(Student):
    """Класс лекторы"""

    def __init__(self, name, surname):
        super().__init__(self, name, surname)

    def rate_lecture(self, mentor, student, course, grade):
        if isinstance(mentor, Mentor) and course in mentor.courses_attached and course in student.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    """Эксперты, проверяющие домашние задания"""

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Выставление оценки преподавателем студенту за курс"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"\nИмя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']

best_student_2 = Student('Ivan', 'Dvornichenko', 'men')
best_student_2.courses_in_progress += ['Python']

best_student_3 = Student('Ulia', 'Smirnova', 'women')
best_student_3.courses_in_progress += ['Python']
best_student_3.courses_in_progress += ['C++']
best_student_3.courses_in_progress += ['C#']
best_student_3.courses_in_progress += ['Kotlin']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['C++']

cool_mentor_3 = Mentor('Ilia', 'Pestov')
cool_mentor_3.courses_attached += ['Python']
cool_mentor_3.courses_attached += ['C#']
cool_mentor_3.courses_attached += ['C++']
cool_mentor_3.courses_attached += ['Kotlin']

cool_mentor_2 = Mentor('Anna', 'Pestova')
cool_mentor_2.courses_attached += ['Python']
cool_mentor_2.courses_attached += ['C#']

cool_mentors = Reviewer('Some', 'Buddy')
cool_mentors.courses_attached += ['Python']
cool_mentors.courses_attached += ['C++']

cool_mentors_3 = Reviewer('Ilia', 'Pestov')
cool_mentors_3.courses_attached += ['Python']
cool_mentors_3.courses_attached += ['C#']
cool_mentors_3.courses_attached += ['C++']
cool_mentors_3.courses_attached += ['Kotlin']

cool_mentors_2 = Reviewer('Anna', 'Pestova')
cool_mentors_2.courses_attached += ['Python']
cool_mentors_2.courses_attached += ['C#']

cool_mentors.rate_hw(best_student, 'Python', 10)
cool_mentors.rate_hw(best_student, 'C++', 2)
cool_mentors_3.rate_hw(best_student_2, 'Python', 7)
cool_mentors_3.rate_hw(best_student_3, 'Python', 7)
cool_mentors_3.rate_hw(best_student_3, 'C#', 10)
cool_mentors_3.rate_hw(best_student_3, 'C++', 8)
cool_mentors_3.rate_hw(best_student_3, 'Kotlin', 5)

cool_lector = Lecture('Ruoy', 'Eman')
cool_lector.rate_lecture(cool_mentor, best_student, 'Python', 7)
cool_lector.rate_lecture(cool_mentor, best_student, 'C++', 1)

cool_lector_2 = Lecture('Ulia', 'Smirnova')
cool_lector_2.rate_lecture(cool_mentor_3, best_student_3, 'Python', 7)
cool_lector_2.rate_lecture(cool_mentor_3, best_student_3, 'C++', 1)
cool_lector_2.rate_lecture(cool_mentor_3, best_student_3, 'C#', 8)
cool_lector_2.rate_lecture(cool_mentor_3, best_student_3, 'Kotlin', 5)

cool_lector_3 = Lecture('Ulia', 'Smirnova')
cool_lector_3.rate_lecture(cool_mentor_2, best_student_3, 'Python', 7)
cool_lector_3.rate_lecture(cool_mentor_2, best_student_3, 'C#', 5)


print("\nВывод информации у студентов")
print(best_student)
print(best_student_2)
print(best_student_3)
print("\nВывод информации у проверяющих")
print(cool_mentors)
print(cool_mentors_3)
print(cool_mentors_2)
print("\nВывод информации у лекторов")
print(cool_mentor)
print(cool_mentor_3)
print(cool_mentor_2)

print()
print("Cравнение (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания")
var_student_1 = best_student < best_student_3
var_student_2 = best_student_2 < best_student

var_mentor_1 = cool_mentor < cool_mentor_3
var_mentor_2 = cool_mentor_2 < cool_mentor_3


def average_student():
    average_student = {}
    for student in students:
        student_dict = student.__dict__["grades"]
        for course in courses:
            if course in student_dict:
                if course in average_student:
                    average_student[course] += student_dict[course]
                else:
                    average_student[course] = student_dict[course]
            else:
                continue
    print()
    for key, val in average_student.items():
        ave = sum(val) / len(val)
        print(f"Cредняя оценка за домашние задания по всем студентам в рамках курса {key} = {ave}")


def average_lector():
    average_lector = {}
    for lector in lectors:
        lector_dict = lector.__dict__["grades"]
        for course in courses:
            if course in lector_dict:
                if course in average_lector:
                    average_lector[course] += lector_dict[course]
                else:
                    average_lector[course] = lector_dict[course]
            else:
                continue
    print()
    for key, val in average_lector.items():
        ave = sum(val) / len(val)
        print(f"Cредняя оценка за домашние задания по всем преподавателям в рамках курса {key} = {ave}")


students = [best_student, best_student_2, best_student_3]
lectors = [cool_mentor, cool_mentor_2, cool_mentor_3]
courses = ['Python', 'C#', 'C++', 'Kotlin']

average_student()
average_lector()

