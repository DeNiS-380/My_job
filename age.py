x = int(input("Введите Ваш возраст: "))
if x >= 18:
    print("Доступ разрешен ")
elif x <= 0:
    print("Данные введены некорректно ")
else:
    print("Доступ запрещен ")
