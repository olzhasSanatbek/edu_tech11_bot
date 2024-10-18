import matplotlib.pyplot as plt

class AnalyticsSystem:
    def __init__(self):
        self.student_progress = {}  # Прогресс студентов по курсам и тестам

    #Добавить студента в систему аналитики
    def add_student(self, student_id):
        if student_id not in self.student_progress:
            self.student_progress[student_id] = {'courses': {}, 'tests': []}
        else:
            print(f"Студент с ID {student_id} уже существует в системе аналитики.")

    #Обновить прогресс по курсу
    def update_course_progress(self, student_id, course_name, progress):
        if student_id in self.student_progress:
            self.student_progress[student_id]['courses'][course_name] = progress
            print(f"Прогресс студента {student_id} по курсу '{course_name}' обновлен до {progress}%.")
        else:
            print(f"Студент с ID {student_id} не найден в системе.")

    #добавить результат теста
    def add_test_result(self, student_id, score):
        if student_id in self.student_progress:
            self.student_progress[student_id]['tests'].append(score)
            print(f"Результат теста {score}% добавлен для студента {student_id}.")
        else:
            print(f"Студент с ID {student_id} не найден.")

    #создать отчет по студенту
    def generate_report(self, student_id):
        if student_id in self.student_progress:
            courses = self.student_progress[student_id]['courses']
            tests = self.student_progress[student_id]['tests']

            print(f"Отчет по студенту {student_id}:")
            print("Прогресс по курсам:")
            for course, progress in courses.items():
                print(f"- {course}: {progress}%")

            if tests:
                print(f"Средний результат по тестам: {sum(tests) / len(tests)}%")
            else:
                print("Тесты не найдены.")

    #построить график прогресса студента 
    def plot_progress(self, student_id):
        if student_id in self.student_progress:
            courses = self.student_progress[student_id]['courses']
            if courses:
                plt.bar(courses.keys(), courses.values())
                plt.xlabel('Курсы')
                plt.ylabel('Прогресс (%)')
                plt.title(f'Прогресс студента {student_id} по курсам')
                plt.show()
            else:
                print("Нет данных для построения графика.")
        else:
            print(f"Студент с ID {student_id} не найден.")
