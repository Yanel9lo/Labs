age = 20

has_access = False

print("Возраст:", age)
print("Допуск имеется:", has_access)

if age >= 18 and has_access == True:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")