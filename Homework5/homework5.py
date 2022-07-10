import Levenshtein

#Отделила определение класса двумя пустыми строками вместо одной
#Использовала 4 пробела на каждый уровень отступа вместо tab


class LevenshteinDistance:

    def words_is_match(word1, word2):
        print(word1, word2, Levenshtein.distance(word1, word2), )

if __name__ == "__main__":

    # Значения в списке pairs расположены двух под другом, а не в одну строку, так как одна строка была бы слишком широкой
    # Закрывающая скобка в списке pairs расположена под первым символом строки, начинающей многострочную конструкцию

    pairs = [
        ('kitting', 'sitting'),
        ('saturday', 'sunday'),
        ('море', 'гора'),
        ('компьютер', 'компьютеры'),
        ('рука', 'рука'),
    ]

    for s, t in pairs:
        LevenshteinDistance.words_is_match(s, t)

#