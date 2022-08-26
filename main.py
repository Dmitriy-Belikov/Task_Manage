import random
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
random - добавлять случайную задачу на дату Сегодня"""

RANDOM_TASKS = ['Записаться на курс Нетологии', 'Сходить в парикмахерскую', 'Помыть машину', 'Убраться в квартире']
tasks = {

}

run = True
#Функция добавления задачи с проверкой словаря
def add_todo(date, task):
    if date in tasks:
        #Дата есть в словаре
        #Добавляем в сисок задачу
        tasks[date].append(task)
    else:
        #Даты в словаре нет
        #создаем запись с ключом date
        tasks[date] = []
        tasks[date].append(task)
    print('Задача ', task, ' добавлена на дату ', date)


while run:
    command = input("Введи команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input('Введите дату для отображения списка задач ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print('Такой даты нет')
    elif command == "add":
        task = input("Введите название задачи: ")
        date = input("Когда выполнить задачу? ")
        add_todo(date, task)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo('Сегодня', task)
    #elif command == "random_date":
    #    add_todo(RANDOM_DATE, RANDOM_TASKS)
    else:
        print('Неизвестная команда')
        break
print('До свидания!')