import numpy as np

# Генерируем случайное число от 1 до 100
number = np.random.randint(1, 101)
def game_v3(number: int = 1) -> int:
    """_summary_

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    # Начальное значение количества попыток
    count = 0   
    # Нижний предел
    min = 0
    # Верхний предел
    max = 100
    while True:
        # Находим срединное значение между пределами
        predict = round((min+max)/2)
        # Увеличиваем количество попыток на 1
        count += 1
        # Если сгенерированное случайное число равно 
        # серединному
        if number == predict:
            # Выходим из цикла
            break
        # Если число больше приравниваем нижний предел 
        # к серединному значения
        elif number > predict:
            min = predict
            print(f"Угадываемое число больше {predict}")
        # Если число меньше приравниваем верхний предел 
        # к серединному значению     
        elif number < predict:
            max = predict 
            print(f"Угадываемое число меньше {predict}")
    print(f"Вы угадали число {number} за {count} попыток. ")

game_v3(number)
