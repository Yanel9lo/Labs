n = int(input("Введите количество измерений: "))
sum = 0.0

for i in range(n):
    value = float(input("Введите значение: "))
    sum += value

if n > 0:
    print("Сумма:", sum)
    print("Среднее:", sum / n)
else:
    print("Ошибка")