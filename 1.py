from random import randint
from time import sleep

def generatee(value1, value2):
    return randint(value1, value2)

a = int(input('Введите число от:'))
b = int(input('Введите число до:'))

result = generatee(a, b)

print(f"Подбираем число в диапозоне от {a} до {b}...")
sleep(1)
print(f"Секунду...")
sleep(1)
print(f"Случайное число: {result}")
