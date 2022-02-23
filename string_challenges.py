# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = set(['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я'])
q_ty = [letter for letter in word.lower() if letter in vowels]
print(len(q_ty))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
[print(word[0]) for word in sentence.split()]


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
len_list = [len(word) for word in sentence.split()]
print(sum(len_list) / len(len_list))
