print("Добро пожаловать в поисковик новомодных слов")
print("Введите непонятное вам слово ниже и получите объяснение")
meme_dict = {
    "КРИНЖ": "Что-то очень странное или стыдное",
    "ЛОЛ": "Что-то очень смешное"
}

meme_list = ["РОФЛ", "шутка", "ЩИЩ", "одобрение или восторг",
             "КРИПОВЫЙ", "страшный, пугающий", "АГРИТЬСЯ", "злиться"]
meme_dict[meme_list[0]] = meme_list[1]
meme_dict[meme_list[2]] = meme_list[3]
meme_dict[meme_list[4]] = meme_list[5]

while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Такого слова в списке нет")
    vopros = input("""Хотите продолжить?:
ДА/НЕТ""")
    if vopros == "ДА" or vopros == "Да" or vopros == "дА" or vopros == "да":
        continue
    else:
        print("Хорошо, досвидания")
        break
