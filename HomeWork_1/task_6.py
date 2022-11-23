"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил "a" километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат
спортсмена составит не менее "b" километров.
Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

"""


def find_day_when_reach_goal(first_day, goal):
    """find the day when sportsmen reach the goal"""
    count = 1
    ans = first_day
    while goal > ans:
        print(f"{count}-й день: {round(ans, 2)}")
        ans *= 1.1
        count += 1
    print(f"{count}-й день: {round(ans, 2)}")
    print(f"Answer: {count} days sportsman reach goal - more than {goal} km.")


a = int(input("First day jogging km = "))
b = int(input("Goal km = "))
find_day_when_reach_goal(a, b)
