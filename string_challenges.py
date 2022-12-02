# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
from collections import Counter

word = 'Архангельск'
cnt = Counter(word.lower())
print(cnt['а'])



# Вывести количество гласных букв в слове
word = 'Архангельск'
num_vowels = 0
vowels = ['а', 'о', 'у', 'и', 'э', 'е', 'ё', 'ы', 'ю', 'я']
for lit in word.lower():
    if lit in vowels:
        num_vowels += 1
print(num_vowels)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = {}
for word in sentence.split():
    words[word] = len(word)
print(sum(words.values()) / len(words))
