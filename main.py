from bloom_filter import BloomFilter

if __name__ == "__main__":
    while True:
        print("Введите длину желаемого фильтра (желательная минимальная длина 16)")
        n = int(input())
        my_array = BloomFilter(n)
        while True:
            print("Что хотите сделать? Выберите нужную цифру")
            print("1 - Добавить слово")
            print("2 - Проверить наличие слова в массиве")
            print("3 - Посмотреть массив и фильтр")
            print("4 - Очистить массив")
            a = int(input())
            while a > 4:
                a = int(input())
            if a == 1:
                print("Введите слово, которое хотите добавить")
                word = input()
                my_array.add(word)
                print(f"Готово!🍰")
            elif a == 2:
                print("Введите слово, которое хотите проверить")
                word = input()
                res = my_array.check_filter(word)
                if res == False:
                    print("Такого слова нет(")
                else:
                    print(
                        f"Такое слово скорее всего есть в масссиве, вероятность ошибки: {res}"
                    )
            elif a == 3:
                print(my_array)
            elif a == 4:
                break
