import Levenshtein

class LevenshteinDistance:

    def words_is_match(word1, word2):
            print(word1, word2, Levenshtein.distance(word1, word2), )

if __name__ == "__main__":

    pairs = [
        ('kitting', 'sitting'),
        ('saturday', 'sunday'),
        ('море', 'гора'),
        ('компьютер', 'компьютеры'),
        ('рука', 'рука'),
    ]

    for s, t in pairs:
        LevenshteinDistance.words_is_match(s, t)