class RewardSystem:
    def __init__(self):
        self.student_rewards = {}  # Словарь для хранения токенов студентов

    #Добавить нового студента в систему вознаграждений
    def add_student(self, student_id):
        if student_id not in self.student_rewards:
            self.student_rewards[student_id] = 0
        else:
            print(f"Студент с ID {student_id} уже существует.")

    #Добавить токены студенту
    def add_tokens(self, student_id, tokens):
        if student_id in self.student_rewards:
            self.student_rewards[student_id] += tokens
            print(f"{tokens} токенов добавлено студенту {student_id}. Всего токенов: {self.student_rewards[student_id]}")
        else:
            print(f"Студент с ID {student_id} не найден.")

    #Получить количество токенов студента
    def get_tokens(self, student_id):
        return self.student_rewards.get(student_id, 0)

    #Использовать токены для получения наград 
    def use_tokens(self, student_id, tokens):
        if student_id in self.student_rewards and self.student_rewards[student_id] >= tokens:
            self.student_rewards[student_id] -= tokens
            print(f"{tokens} токенов использовано студентом {student_id}. Остаток токенов: {self.student_rewards[student_id]}")
        else:
            print(f"Недостаточно токенов или студент с ID {student_id} не найден.")
