from datetime import datetime
import random
import re

# Перше завдання
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

def get_days_from_today(date):
    try:
        # перетворюємо рядок в об'єкт datetime
        string_to_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        difference = today_date - string_to_date
        return difference.days
    except ValueError:
        return "Дату введено не коректно"


date = "2025.10.11"
print("1)", get_days_from_today(date))


# Друге завдання
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
# Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min < 1 or max > 1000 or max < min or max-min < quantity:
        return []        
    else:
        # sample - повертає список довжиною k унікальних елементів випадково вибраних з range(min, max+1)(діапазон з min до max включно(додали 1)), sorted - сортує
        return sorted(random.sample(range(min, max+1), quantity))

lottery_numbers = get_numbers_ticket(10, 15, 9)
print("2) Ваші лотерейні числа:", lottery_numbers)

# Третє завдання(не обов'язкове)
# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи 
# тільки цифри та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі 
# та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду, 
# функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.

def normalize_phone(phone_number):
    # видаляємо все окрім цифр
    phone_number = re.sub(r"[^\d]", "", phone_number)
    # замінюємо перші(першу) цифри(цифру)(що йдуть перед 9 іншими) на +380
    phone_number = re.sub(r"\d+(?=\d{9})", "+380", phone_number)
    return phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("3) Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
