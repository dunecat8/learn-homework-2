# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ('а','е', 'и', 'о', 'у', 'э', 'ы', 'ю', 'я')
result = [i for i in list(word.lower()) if i in vowels]
print(len(result))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
total_chars = len(sentence.replace(' ', ''))
wordcount = len(sentence.split())
result = total_chars / wordcount
print(result)