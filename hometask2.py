#2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f'{x = } {y = } {z = } выражение: {not (x or y or z) == (not x and not y and not z)}')