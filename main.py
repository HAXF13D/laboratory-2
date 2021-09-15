string = input("Введите строку: ").split()
length = int(input("Введите длину слова: "))
count = 0
for word in string:
    if len(word) >= length:
        count += 1
print(f"Количество слов, длина которых >= {length} = {count}")
