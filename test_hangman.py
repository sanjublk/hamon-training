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


def test_mask_word_invalid_guesses():
    for i in ["police", "elephant", "it", "foo"]:
        assert hangman.mask_word(i, ["x", "q"]) == len(i) * "-"


def test_mask_word_single_guesses():
    assert hangman.mask_word('football', ['b']) == '----b---'
    assert hangman.mask_word('orange', ['o']) == 'o-----'
    assert hangman.mask_word('basketball', ['k']) == '---k------'


def test_mask_multiple_guess():
    secret_word = "elephant"
    guessed_letters = ["e", "p"]
    assert hangman.mask_word(secret_word, guessed_letters) == "e-ep----"
    guessed_letters.append("z")
    assert hangman.mask_word(secret_word, guessed_letters) == "e-ep----"
    assert hangman.mask_word('madam', ['m', 'a', 'd']) == 'madam'
    assert hangman.mask_word('madam', ['m', 'a', 'd', 'm']) == 'madam'
    assert hangman.mask_word('madam', ['m', 'a', 'd', 'm', '']) == 'madam'
    

# RED - Implement a test that will fail
# GREEN - Make the test pass
# refactoR - Adjust the code so that all tests pass and code is improved
