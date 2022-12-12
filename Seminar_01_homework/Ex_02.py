# Ex_2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения not (x[0] or x[1] or x[2] = not 
# x[0] and not x[1] and not x[2]) для всех значений предикат. 

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print (True)
else:
    print (False)