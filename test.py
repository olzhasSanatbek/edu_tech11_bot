from RewardSystem import RewardSystem
from analyticsSystem import AnalyticsSystem

# Инициализация систем вознаграждений и аналитики
reward_system = RewardSystem()
analytics_system = AnalyticsSystem()

# Добавление студента
student_id = 123
reward_system.add_student(student_id)
analytics_system.add_student(student_id)

# Добавление прогресса по курсу
analytics_system.update_course_progress(student_id, "Python Programming", 50)
analytics_system.update_course_progress(student_id, "Data Science", 70)

# Добавление результатов тестов
analytics_system.add_test_result(student_id, 85)
analytics_system.add_test_result(student_id, 90)

# Начисление токенов за прогресс
reward_system.add_tokens(student_id, 50)  # 50 токенов за прогресс

# Использование токенов для награды
reward_system.use_tokens(student_id, 20)  # Использование 20 токенов

# Генерация отчета
analytics_system.generate_report(student_id)

# Построение графика прогресса
analytics_system.plot_progress(student_id)
