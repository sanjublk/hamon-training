import random


def get_random_word(path="/usr/share/dict/words"):
    words = []
    with open(path, "r") as f:
        for word in f.readlines():
            word = word.strip()
            if len(word) <= 6:
                continue
            if not word.isalpha():
                continue
            if word[0].isupper():
                continue
            words.append(word)
    return random.choice(words)


def mask_word(secret_word, guessed_letters):
    masked_word = ""
    for c in secret_word:
        if c in guessed_letters:
            masked_word += c
        else:
            masked_word += "-"
    return masked_word


if __name__ == "__main__":
    pass
