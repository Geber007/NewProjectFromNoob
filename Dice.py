import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    print("Симулятор игры в кости")
    
    while True:
        input("Нажмите Enter, чтобы бросить кубики...")
        die1, die2 = roll_dice()
        total = die1 + die2
        print(f"Вы бросили: {die1} и {die2}. Сумма: {total}.")
        
        play_again = input("Хотите бросить еще раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            break

    print("Спасибо за игру!")

if __name__ == "__main__":
    main()
