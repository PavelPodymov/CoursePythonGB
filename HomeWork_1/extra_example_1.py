"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
*Пример:*
- 6 -> да
- 7 -> да
- 1 -> нет
"""


def check_weekend(day):
    """Check the day - weekend or no from number"""
    if 1 > day > 7:
        print("You write wrong number")
    elif day < 6:
        print(f"- {day} -> No.")
    else:
        print(f"- {day} -> Yes! WeekEND!")


try:
    some_day = int(input("Please input number from 1 to 7: "))
    check_weekend(some_day)
except ValueError:
    print("You write wrong number")
