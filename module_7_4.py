# Домашнее задание по теме "Форматирование строк".

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %:
print('В команде Мастера кода участников: %s !' % team1_num)
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "

print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"

# Использование format():
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"

print('Волшебники данных решили задачи за {} с !'.format(team1_time))
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
# Пример итоговой строки: "Команды решили 40 и 42 задач.”

print(f'Результат битвы: {challenge_result}')
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
