import random

import hangman

random.seed(10)


def test_get_random_word_min_length_6():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ["ambulances", "cat", "car", "dog", "hen"]:
            f.write(i + "\n")
    word = hangman.get_random_word(my_dict)
    assert word == "ambulances"


def test_get_random_word_no_non_alphanum():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ["elephants", "hospital's", "policeman's"]:
            f.write(i + "\n")
    word = hangman.get_random_word(my_dict)
    assert word == "elephants"


def test_get_random_word_no_proper_noun():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ["firehouse", "Abraham", "Mercury"]:
            f.write(i + "\n")
    word = hangman.get_random_word(my_dict)
    assert word == "firehouse"


def test_get_random_word():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ["ambulances", "hospitalized", "car", "Abraham", "mercury's"]:
            f.write(i + "\n")
    words = set()
    for _ in range(10):
        word = hangman.get_random_word(my_dict)
        words.add(word)
    assert words == {"hospitalized", "ambulances"}


def test_mask_word_no_guesses():
    for i in ["police", "elephant", "it", "foo"]:
        assert hangman.mask_word(i, []) == len(i) * "-"


def test_mark_word_invalid_guesses():
    for i in ["police", "elephant", "it", "foo"]:
        assert hangman.mask_word(i, ["x", "q"]) == len(i) * "-"


def test_mask_word_single_guesses():
    assert hangman.mask_word("football", ["b"]) == "----b---"
    assert hangman.mask_word("orange", ["o"]) == "o-----"
    assert hangman.mask_word("basketball", ["k"]) == "---k------"


def test_mask_word_repeated_char():
    secret_word = "elephant"
    guessed_letters = ["e", "p"]
    assert hangman.mask_word(secret_word, guessed_letters) == "e-ep----"

    assert hangman.mask_word("madam", ["m", "a", "d"]) == "madam"


def test_get_status_when_lost():
    secret_word = 'amazon'
    guessed_letters = None
    turns_left = None
    result = hangman.LOST
    status = """You lost 👎
The secret word is amazon"""
    assert hangman.get_status(secret_word, guessed_letters, turns_left, result) == status


def test_get_status_when_won():
    secret_word = 'amazon'
    guessed_letters = None
    turns_left = None
    result = hangman.WON
    status = """You won 👍
The secret word is amazon"""
    assert hangman.get_status(secret_word, guessed_letters, turns_left, result) == status


def test_get_status_when_good_guess():
    secret_word = 'monkey'
    guessed_letters = list('mon')
    turns_left = 3
    result = hangman.GOOD_GUESS

    status = f"""turns_left: {turns_left}
guessed_letters: m o n
mon---"""
    assert hangman.get_status(secret_word, guessed_letters, turns_left, result) == status


def test_get_status_when_bad_guess():
    secret_word = 'monkey'
    guessed_letters = list('mon')
    turns_left = 3
    result = hangman.BAD_GUESS

    status = f"""turns_left: 3
guessed_letters: m o n
mon---"""
    assert hangman.get_status(secret_word, guessed_letters, turns_left, result) == status


def test_get_status_when_already_guessed():
    secret_word = 'monkey'
    guessed_letters = list('mon')
    turns_left = 3
    result = hangman.ALREADY_GUESSED

    status = f"""You already guessed that letter\nturns_left: 3
guessed_letters: m o n
mon---"""
    assert hangman.get_status(secret_word, guessed_letters, turns_left, result) == status

def test_process_turn_already_guessed():
    current_guess = "s"
    secret_word = "secret"
    guessed_letters = list("se")
    turns_left = 4

    assert hangman.process_turn(
        current_guess, secret_word, guessed_letters, turns_left
    ) == (turns_left, guessed_letters, hangman.ALREADY_GUESSED)


def test_process_turn_game_won():
    current_guess = "a"
    secret_word = "amazing"
    guessed_letters = list("mzing")
    turns_left = 4
    assert hangman.process_turn(
        current_guess, secret_word, guessed_letters, turns_left
    ) == (turns_left, guessed_letters, hangman.WON)


def test_process_turn_game_lost():
    current_guess = 'b'
    secret_word = 'amazing'
    guessed_letters = list('mzing')
    turns_left = 1

    assert hangman.process_turn(
        current_guess, secret_word, guessed_letters, turns_left
    ) == (turns_left, guessed_letters, hangman.LOST)


def test_process_turn_bad_guess():
    current_guess = 'x'
    secret_word = 'wallaby'
    guessed_letters = list('lla')
    turns_left = 2
    assert hangman.process_turn(
        current_guess, secret_word, guessed_letters, turns_left
    ) == (turns_left - 1, guessed_letters + ['x', ], hangman.BAD_GUESS)


def test_process_turn_good_guess():
    current_guess = 'b'
    secret_word = 'wallaby'
    guessed_letters = list('lla')
    turns_left = 2
    assert hangman.process_turn(
        current_guess, secret_word, guessed_letters, turns_left
    ) == (turns_left, guessed_letters + ['b', ], hangman.GOOD_GUESS)

# RED - Implement a test that will fail
# GREEN - Make the test pass
# REFACTOR - Adjust the code so that all tests pass and code is improved
