"""
HomeWork 1 extra_example_2.py
Напишите программу для проверки истинности утверждения:
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
v = or
¬ - not
⋀ - and

"""


def input_numbers():
    """input the numbers 'X', 'Y', 'Z'"""
    xyz = ["X", "Y", "Z"]
    list_number = [int(input(f"Input number: {xyz[i]}: ")) for i in range(3)]
    return list_number


def check_predicate(lst):
    """check predicate"""
    left = not (lst[0] or lst[1] or lst[2])
    right = not lst[0] and not lst[1] and not lst[2]
    if left == right:
        return True
    else:
        return False

# print(check_predicate(input_numbers()))
