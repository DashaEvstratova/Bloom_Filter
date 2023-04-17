from helper_funktion import add_text_in_bloom_filter

if __name__ == "__main__":
    print("Введите текст: ")
    text = input()
    my_array = add_text_in_bloom_filter(text)
    while True:
        print("Введите слово, наличие которого хотите проверить: ")
        word = input()
        res = my_array.check_filter(word)
        if res == False:
            print("Такого слова нет(")
        else:
            print(
                f"Такое слово скорее всего есть в масссиве, вероятность ошибки: {res}")
