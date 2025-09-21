import random

class GuessIt:
    def __init__(self):
        self.winCond = False
        self.word_lst = [
            "about", "alert", "argue", "beach", "begin", "black", "blame", "blind", "board", "brain",
            "bread", "break", "brown", "build", "camel", "chair", "chart", "chase", "cheap", "check",
            "chest", "chief", "child", "china", "claim", "class", "clean", "clear", "clock", "close",
            "coach", "coast", "could", "count", "court", "crane", "cream", "crime", "cross", "crowd",
            "crown", "cycle", "daily", "dance", "death", "depth", "doubt", "dozen", "draft", "drama",
            "dream", "dress", "drink", "drive", "earth", "enemy", "enter", "error", "event", "faith",
            "fault", "field", "fight", "final", "floor", "focus", "force", "frame", "frank", "front",
            "fruit", "glass", "grant", "grass", "green", "group", "guard", "guess", "guide", "heart",
            "henry", "horse", "hotel", "house", "image", "index", "input", "issue", "japan", "jones",
            "judge", "knife", "laura", "layer", "level", "lewis", "light", "limit", "lunch", "major",
            "march", "match", "metal", "model", "money", "month", "motor", "mouth", "music", "night"
        ]
        self.mod_word_lst = [i.upper() for i in self.word_lst]
        self.ranWord = random.choice(self.mod_word_lst)
        # print(self.ranWord)
        self.play()

    def guess_It(self):
        while True:
            guess = input("_____\n")

            if not guess.isalpha():
                print("Try again.(Use alphabetic characters)")
                continue

            if len(guess) != 5:
                print("Try again.(Invalid Size of Guess)")
                continue

            if guess.upper() not in self.mod_word_lst:
                print("Try again.(Word not in our dictionary)")
                continue

            return guess

    def guess_Checker(self, guess):
        feedback = [''] * 5
        ranWord_copy = list(self.ranWord)

        for i in range(5):
            if guess[i] == ranWord_copy[i]:
                feedback[i] = '🟩'
                ranWord_copy[i] = None

        for i in range(5):
            if feedback[i] == '':
                if guess[i] in ranWord_copy:
                    feedback[i] = '🟨'
                    ranWord_copy[ranWord_copy.index(guess[i])] = None
                else:
                    feedback[i] = '⬛'

        print("Your feedback:", " ".join(feedback))
        return self.ranWord == guess

    def play(self):
        guesses_left = 6
        victory = False

        while guesses_left > 0 and not victory:
            print(f"You have {guesses_left} guesses left.")

            guess = self.guess_It()
            victory = self.guess_Checker(guess.upper())
            guesses_left -= 1

        if victory:
            print("Congrats you have guessed it, you won!")
        else:
            print(f"You lost! The secret word was {self.ranWord}")

game = GuessIt()
