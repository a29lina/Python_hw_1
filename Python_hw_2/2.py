# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
counter = 1
prod = 1
while counter <= number:
    prod *= counter
    print(prod, end= ' ')
    counter += 1
print()
print('Произведение чисел от 1 до N =', prod)
