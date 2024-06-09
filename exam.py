# Напишете програма, която да пресмята статистика за оценки от изпит.
# В началото програмата получава броя на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да отпечата процента студенти с оценка
# между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също така и средния успех на изпита.
# Вход:
# От конзолата се четат:
# •	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# •	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход:
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -	"Fail: {по-малко от 3.00}%"
# Ред 5 -	"Average: {среден успех}"
# Всички числа трябва да са форматирани до втория знак след десетичната запетая.


students_count = int(input())
top_students = 0
between_4_and_4_99 = 0
between_3_and_3_99 = 0
fail_students = 0
total_grades = 0

for _ in range(students_count):
    grade = float(input())
    total_grades += grade

    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        between_4_and_4_99 += 1
    elif 3.00 <= grade <= 3.99:
        between_3_and_3_99 += 1
    else:
        fail_students += 1
top_students_percentage = (top_students / students_count) * 100
between_4_and_4_99_percentage = (between_4_and_4_99 / students_count) * 100
between_3_and_3_99_percentage = (between_3_and_3_99 / students_count) * 100
fail_students_percentage = (fail_students / students_count) * 100
average_grade = total_grades / students_count

print(f"Top students: {top_students_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_4_99_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_3_99_percentage:.2f}%")
print(f"Fail: {fail_students_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
