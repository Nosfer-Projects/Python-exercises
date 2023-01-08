


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