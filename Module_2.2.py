first = (int(input('Первое число:')))
second = (int(input('Второе число:')))
third = (int(input('Третье число:')))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first != second != third:
    print(0)