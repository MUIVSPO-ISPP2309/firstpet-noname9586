import random

def generate_number(lower, upper):
    return random.randint(lower, upper)

def get_guess():
    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            return guess
        except ValueError:
            print("Пожалуйста, введите целое число.")

def play_game(lower, upper, max_attempts):
    number_to_guess = generate_number(lower, upper)
    attempts = 0

    print(f"Я загадал число от {lower} до {upper}. У вас есть {max_attempts} попыток.")

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1
        
        if guess < number_to_guess:
            print("Больше!")
        elif guess > number_to_guess:
            print("Меньше!")
        else:
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
            return

    print(f"Вы исчерпали все попытки! Загаданное число было {number_to_guess}.")

def main():
    print("Добро пожаловать в игру 'Угадай число'!")

    while True:
        lower = int(input("Введите нижнюю границу диапазона: "))
        upper = int(input("Введите верхнюю границу диапазона: "))
        max_attempts = int(input("Введите максимальное количество попыток: "))
        
        play_game(lower, upper, max_attempts)

        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            break

if __name__ == "__main__":
    main()
