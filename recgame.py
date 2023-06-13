import random
import time
import pygame
import os

score = 0

def generate_task(difficulty):
    if difficulty == 3:
        return random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    else:
        return random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])


# Функция для воспроизведения музыки в главном меню
def play_menu_music():
    # Инициализация Pygame.mixer
    pygame.mixer.init()

    # Загрузка и воспроизведение музыки
    menu_music = pygame.mixer.music.load("intro music.mp3")
    pygame.mixer.music.play(-1)

# Установка громкости музыки (0.5 - половина максимальной громкости)
    pygame.mixer.music.set_volume(0.1)

# Воспроизведение музыки в главном меню
play_menu_music()

def play_game(difficulty):
    global score
    time_limit = 4 - difficulty + 1

    pygame.mixer.init()

    music_file = ""
    if difficulty == 1:
        print("Уровень: Легкий")
        music_file = "ez .mp3"
    elif difficulty == 2:
        print("Уровень: Средний")
        music_file = "medium.mp3"
    elif difficulty == 3:
        print("Уровень: Сложный")
        music_file = "hard.mp3"
        # Установка громкости музыки (0.5 - половина максимальной громкости)
        pygame.mixer.music.set_volume(0.1)

    music_path = os.path.join(os.getcwd(), music_file)
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()

    while score < 100:
        task = generate_task(difficulty)
        print("Задание: Введите", task)
        start_time = time.time()
        user_input = input()

        if user_input == task:
            end_time = time.time()
            elapsed_time = end_time - start_time

            if elapsed_time <= time_limit:
                score += 1
                print("Верно!")
                print("Ваш текущий счет:", score)
            else:
                print("Время истекло!")
        else:
            print("Неправильно!")

        print()

    pygame.mixer.music.stop()
    print("Вы достигли счета 100!")

def select_difficulty():
    print("Выберите сложность:")
    print("1. Легкий")
    print("2. Средний")
    print("3. Сложный")

    difficulty = int(input("Введите номер сложности: "))
    while difficulty not in [1, 2, 3]:
        print("Неверный выбор сложности!")
        difficulty = int(input("Введите номер сложности: "))

    return difficulty

selected_difficulty = select_difficulty()
play_game(selected_difficulty)
