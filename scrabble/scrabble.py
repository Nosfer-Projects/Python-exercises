# Below is the score set for the English version:

# empty tile - 0 points (usually two in a set)

# EAIONRTLSU - 1 pt

# DG - 2 points

# BCMP - 3 pts

# FHVWY - 4 pts

# K - 5 pts

# JX - 8 pts

# QZ - 10 pts

# Implement a function called score() that will return the score for the word you composed. We assume that the given word is grammatically correct. For simplicity, an empty tile can be represented as a space character ' '.


def score(main_string):
    score_dict = {
        0: [" "],
        1: ["e", "a", "i", "o", "n", "r", "t", "l", "s", "u"],
        2: ["d", "g"],
        3: ["b", "c", "m", "p"],
        4: ["f", "h", "v", "w", "y"],
        5: ["k"],
        8: ["j", "x"],
        10: ["q", "z"]
    }
    text = main_string.lower()
    score = 0
    for i in text:
        for key, value in score_dict.items():
            if i in value:
                score += key
                break
    return score

print(score('python'))