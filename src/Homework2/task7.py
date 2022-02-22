"""Для выигрыша главного приза необходимо, чтобы шесть номеров на лотерейном билете совпали
 с шестью числами, выпавшими случайным образом в диапазоне от 1 до 49 во время очередного тиража.
  Напишите программу, которая будет случайным образом подбирать шесть номеров для вашего билета.
   Убедитесь в том, что среди этих чисел не будет дубликатов. Выведите номера билетов на экран по
    возрастанию.
"""

import random

list_1 = [i for i in range(1, 51)]
random.shuffle(list_1)
list_1 = sorted(list_1[:6])
print('Счастливые числа: ' + ', '.join(map(str, list_1)))
