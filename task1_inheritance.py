
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
      
    def rate_hw_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 1 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]    
        else:
            return 'Ошибка' 
    
    def _get_average_count_stud(self):
        sum_stud = 0
        count = 0
        for course in self.grades.values():
            sum_stud += sum(course)
            count += len(course)
        return round(sum_stud / count, 1)
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._get_average_count_stud()}\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {", ".join(self.finished_courses)}'
        return res
    
    def __lt__(self, other_student):
        if isinstance (other_student, Student):
            compare = self._get_average_count_stud() > other_student._get_average_count_stud() 
            if compare:
               return f'Средняя оценка за домашние задания у студента {self.name} {self.surname} выше чем у студента {other_student.name} {other_student.surname}.'
            else:
               return f'Средняя оценка за домашние задания у студента {self.name} {self.surname} ниже чем у студента {other_student.name} {other_student.surname}.'
        else:
            return 'Сравнивать можно толко студентов'

     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
           
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._get_average_count_lect()}'
        return res
    
    def _get_average_count_lect(self):
        sum_lect = 0
        count = 0
        for course in self.grades.values():
            sum_lect += sum(course)
            count += len(course)
        return round(sum_lect / count, 1)
    
    def __lt__(self, other_lecturer):
        if isinstance (other_lecturer, Lecturer):
            compare = self._get_average_count_lect() > other_lecturer._get_average_count_lect() 
            if compare:
               return f'Средняя оценка за лекции у лектора {self.name} {self.surname} выше чем у лектора {other_lecturer.name} {other_lecturer.surname}.'
            else:
               return f'Средняя оценка за лекции у лектора {self.name} {self.surname} ниже чем у лектора {other_lecturer.name} {other_lecturer.surname}.'
        else:
            return 'Сравнивать можно толко лекторов'
  
class Reviewer(Mentor):
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def average_count_one_stud(student_all_list, course):
    average_count = 0
    count = 0
    for student in student_all_list:
        for course_name, grade in student.grades.items():
            if course_name == course:
                average_count += sum(grade) / len(grade)
                count += 1
            else:
                continue
    if count != 0:
        return round(average_count / count, 1)
    else:
        return f'No course {course}'
    
    
    
def average_count_one_lect(lecturer_all_list, course):
    average_count = 0
    count = 0
    for lecturer in lecturer_all_list:
        for course_name, grade in lecturer.grades.items():
            if course_name == course:
                average_count += sum(grade) / len(grade)
                count += 1
            else:
                continue
    if count != 0:
        return round(average_count / count, 1)
    else:
        return f'No course {course}'


norm_student = Student('Toma', 'Sit', 'girl')
norm_student.courses_in_progress += ['DRIVE']
norm_student.courses_in_progress += ['GITHUB']
norm_student.courses_in_progress += ['GIT']
norm_student.finished_courses += ['Введение в программирование']

tom_student = Student('Tom', 'Smit', 'boy')
tom_student.courses_in_progress += ['DRIVE']
tom_student.courses_in_progress += ['GITHUB']
tom_student.courses_in_progress += ['GIT']
tom_student.finished_courses += ['Введение в программирование']

ed_student = Student('Ed', 'Shiran', 'boy')
ed_student.courses_in_progress += ['GITHUB']
ed_student.courses_in_progress += ['DRIVE']
ed_student.courses_in_progress += ['GIT']
ed_student.finished_courses += ['Введение в программирование']

artur_reviewer = Reviewer('Artur', 'Nechaev')
artur_reviewer.courses_attached += ['GITHUB']
artur_reviewer.courses_attached += ['DRIVE']
artur_reviewer.courses_attached += ['GIT']

aleksandr_lecturer = Lecturer('Aleksandr', 'Nesterov')
aleksandr_lecturer.courses_attached += ['GITHUB']
aleksandr_lecturer.courses_attached += ['DRIVE']
aleksandr_lecturer.courses_attached += ['GIT']

ekaterina_lecturer = Lecturer('Ekaterina', 'Kalantaeva')
ekaterina_lecturer.courses_attached += ['GIT']

artur_reviewer.courses_attached += ['GIT']
artur_reviewer.courses_attached += ['GITHUB']
artur_reviewer.courses_attached += ['DRIVE']
artur_reviewer.rate_hw(tom_student, 'GIT', 8)
artur_reviewer.rate_hw(tom_student, 'GIT', 6)
artur_reviewer.rate_hw(ed_student, 'DRIVE', 10)
artur_reviewer.rate_hw(ed_student, 'DRIVE', 7)
artur_reviewer.rate_hw(tom_student, 'GITHUB', 7)
artur_reviewer.rate_hw(tom_student, 'GITHUB', 10)
artur_reviewer.rate_hw(ed_student, 'GITHUB', 6)
artur_reviewer.rate_hw(ed_student, 'GITHUB', 5)
artur_reviewer.rate_hw(norm_student, 'GITHUB', 10)


ed_student.rate_hw_lect(aleksandr_lecturer, 'GITHUB', 9)
ed_student.rate_hw_lect(aleksandr_lecturer, 'DRIVE', 10)
ed_student.rate_hw_lect(ekaterina_lecturer, 'GIT', 9)

tom_student.rate_hw_lect(aleksandr_lecturer, 'GITHUB', 6)

norm_student.rate_hw_lect(aleksandr_lecturer, 'GITHUB', 10)
norm_student.rate_hw_lect(ekaterina_lecturer, 'GIT', 6)


print('Информация о проверяющем')
print(artur_reviewer)

print()
print('Информация о лекторах')
print(aleksandr_lecturer)
print(ekaterina_lecturer)

print()
print('Информация о студентах')
print(tom_student)
print(ed_student)
print(norm_student)

print()
print('Сравнение среднего бала за лекции между лекторами.')
print(aleksandr_lecturer > ekaterina_lecturer)
print('Сравнение среднего бала за домашние задания студентов.')
print(tom_student > ed_student)


print()
print(f'''Средняя оценка лекторов по курсу GITHUB: {average_count_one_lect([aleksandr_lecturer, ekaterina_lecturer], 'GITHUB')}''')
print(f'''Средняя оценка лекторов по курсу GIT: {average_count_one_lect([aleksandr_lecturer, ekaterina_lecturer], 'GIT')}''')
print(f'''Средняя оценка за домашние задания у студентов по курсу GIT: {average_count_one_stud([tom_student, ed_student, norm_student], 'GITHUB')}''')
