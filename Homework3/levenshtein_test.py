import Levenshtein

pairs = [
        ('kitting', 'sitting'),
        ('saturday', 'sunday'),
        ('море', 'гора'),
        ('компьютер', 'компьютеры'),
        ('рука', 'рука'),
    ]

if __name__ == "__main__":
    for s, t in pairs:
        print(s, t, Levenshtein.distance(s, t),)
