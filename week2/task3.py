studentscount = int()
students_average_grades = []
school_grade_average = float()


school = {
    'Младшие Классы':{
        '4а':{
            'Петя':{'Оценки':[3,4,2,3,5]},
            'Оля':{'Оценки':[5,4,4,5,4]},
            'Вася':{'Оценки':[4,3,5,4,3]}
        },
        '4б':{
            'Гена':{'Оценки':[2,5,4,3,5]},
            'Оля':{'Оценки':[5,4,5,5,5]},
            'Света':{'Оценки':[3,5,3,5,3]}
        },
        '4в':{
            'Вася':{'Оценки':[2,2,2,2,3]},
            'Петя':{'Оценки':[5,4,3,4,5]},
            'Вика':{'Оценки':[4,4,4,4,5]}
        }
    },
    'Старшие классы':{
        '10а':{
            'Гена':{'Оценки':[3,4,3,3,4]},
            'Коля':{'Оценки':[5,4,4,2,2]},
            'Ваня':{'Оценки':[2,4,5,3,3]}
        },
        '10б':{
            'Света':{'Оценки':[2,4,2,3,5]},
            'Оля':{'Оценки':[5,4,4,3,5]},
            'Галя':{'Оценки':[3,4,2,3,4]}
        },
        '10в':{
            'Леша':{'Оценки':[3,4,2,3,4]},
            'Леша М':{'Оценки':[4,4,4,4,4]},
            'Кхорг Завоеватель':{'Оценки':[10,10,10,10,10]}
        }
    }
    

}
###Словарь словарей словарей inception
for stage, classnumber in school.items():
    print("\n",stage)

    for classnumber, students in classnumber.items():
        print(classnumber)
        studentscount += len(students)
        class_total_grades = []
        for name, grades in students.items():
            average_grade = sum(grades['Оценки']) / len(grades['Оценки'])
            print("Имя: %s, Оценки: %s, Средняя оценка: %s" % (name,grades['Оценки'],average_grade))
            students_average_grades.append(average_grade)
            class_total_grades.append(average_grade)
        class_average = sum(class_total_grades) / len(students)
        print('Средняя оценка в классе: %s' % (class_average))

def countgrades():
    school_grade_average = sum(students_average_grades) / studentscount
    result = ('\nВсего учеников: %s\nСредняя оцкнка по школе: %s' % (studentscount,school_grade_average))
    return result

print(countgrades())