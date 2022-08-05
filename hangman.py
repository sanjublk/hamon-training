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


def Hangman:
    def __init__(self):
        self.chances = 6
        self.secret = get_random_word()
        self.guessed_letters = {}
        self.masked_word = '-' * len(self.secret)
   
    def game_won():
        if self.secret == self.masked_word:
            return True
        return False
            
    def run():
        print(self.secret + '\t' + self.chances)
        while self.turn == 0:
            guess = input('Enter you guess:').lower()
            if len(guess) != 1 and not guess.isalpha():
                print('You need to enter a single character') 
                continue
            self.guessed_letters.add(guess)
            self.masked_word = mask_word(self.secret, list(guess))
            if self.game_won():
                print('You won')
                return
            self.chances += 1

if __name__ == "__main__":
    pass
