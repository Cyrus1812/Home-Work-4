# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x 
# 2. 3x^2 + x + 8
# Результат: 8x^2 + 4x + 8




def GetFormuls():
    with open("formula.txt","w+",encoding="utf=8") as create:
        create.write(input("Введите значения a,b,c в первой формуле типа 'ax^2 + bx + c', разделив их пробелами: "))
        create.write('\n')
        create.write(input("Введите значения a,b,c во второй формуле типа 'ax^2 + bx + c', разделив их пробелами: "))
GetFormuls()
def ReadFormuls():
    with open("formula.txt",encoding="utf=8") as create:
        formula = (create.readline().split(" ")) 
        formula = [int(i) for i in formula]
        formulaSecond = (create.readline().split(" ")) 
        formulaSecond = [int(i) for i in formulaSecond]
        summ = [ None, None, None ]
        for i in range(0,3):
            summ[i] = formula[i] + formulaSecond[i]
        for j in range(0,1):
            if 0<summ[j]<2 and 0<summ[j+1]<2:
                print(f"x^2 + x + {summ[j+2]}")
            elif summ[j+1]<= 1:
                print(f"{summ[j]}x^2 + x + {summ[j+2]}")
            elif summ[j]<= 1:
                print(f"x^2 + {summ[j+1]}x + {summ[j+2]}")
            else:
                print(f"{summ[j]}x^2 + {summ[j+1]}x + {summ[j+2]}")
ReadFormuls()