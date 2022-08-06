import random

WON = 0
LOST = 1
ALREADY_GUESSED = 2
GOOD_GUESS = 3
BAD_GUESS = 4


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


def get_status(secret_word, guessed_letters, turns_left, result):
    if result in (WON, LOST):
        place_holder = 'won 👍' if result == WON else 'lost 👎'
        return f"""You {place_holder}
    The secret word is {secret_word}"""

    ret = f"""turns_left: {turns_left}
    guessed_letters: {" ".join(guessed_letters)}
    {mask_word(secret_word, guessed_letters)}
    """

    if result == ALREADY_GUESSED:
        ret = "You already guessed that letter\n" + ret
    return ret


def process_turn(current_guess, secret_word, guessed_letters, turns_left):
    if current_guess in guessed_letters:
        return turns_left, guessed_letters, ALREADY_GUESSED
    if secret_word == mask_word(secret_word, guessed_letters + [current_guess, ]):
        return turns_left, guessed_letters, WON
    if turns_left == 1:
        return turns_left, guessed_letters, LOST

    guessed_letters = guessed_letters + [current_guess, ]

    if current_guess not in secret_word:
        turns_left -= 1
        result = BAD_GUESS
    else:
        result = GOOD_GUESS
    return turns_left, guessed_letters, result


def main():
    secret_word = get_random_word()
    turns_left = 7
    guessed_letters = []
    print(secret_word)
    while True:
        print(get_status(secret_word, guessed_letters, turns_left, GOOD_GUESS))
        current_guess = input("guess a letter:")
        turns_left, guessed_letters, result = process_turn(
            current_guess, secret_word, guessed_letters, turns_left
        )
        if result == WON:
            print(get_status(secret_word, guessed_letters, turns_left, result))
            break
        if result == LOST:
            print(get_status(secret_word, guessed_letters, turns_left, result))
            break
        

if __name__ == "__main__":
    main()