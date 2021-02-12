import random
import time
from combinatorics import all_colours

class InvalidMove(Exception):pass

print("Welcome to Mastermind! \n")
print("Please select the mode you would like to play:\n 1. Computer vs Me \n 2. Me vs Computer \n")
choise = int(input("choise: "))

if choise == 1:
    def main():
        class Game:  ###https://www.daniweb.com/programming/software-development/threads/192328/mastermind-game
            def __init__(self):
                self.colors = ('r', 'g', 'b', 'o', 'p', 'z')
                self.to_guess = [random.choice(self.colors) for i in range(4)]  # the secret to guess

            def match_guess(self, guess):
                if len(guess) != len(self.to_guess) or [g for g in guess if g not in self.colors]:
                    raise InvalidMove()
                ret = [0, 0]  # first, black peg: good color good place, second white peg: good
                usedindexes = []  # which place has already given a peg
                for i, g in enumerate(guess):
                    if g == self.to_guess[i]:
                        ret[0] += 1
                        usedindexes.append(i)
                for i, g in enumerate(guess):
                    if i in usedindexes: continue
                    for j, c in enumerate(self.to_guess):
                        if c == g and j not in usedindexes:
                            ret[1] += 1
                            usedindexes.append(j)
                    return ret

            def make_move(self):
                guess = input("Raad: ")
                return guess.split()

            def main(self):
                print("De game begint, de computer bedenkt een code...")
                time.sleep(0.5)
                print("Klaar!")
                print("Mogelijke kleuren (voer alleen eerste letter in): [r]ood [g]roen [b]lauw [p]aars [o]ranje [z]wart")
                print("Voorbeeld invoer: r g b o \n")
                g = Game()
                count = 0
                while True:
                    if count == 8:
                        print("You lose!")
                        print("De code was: ", self.to_guess)
                        break
                    else:
                        guess = self.make_move()
                        count +=1
                        try:
                            bp, wp = g.match_guess(guess)
                        except InvalidMove:
                            print("Ongeldig, probeer opnieuw")
                            continue
                        print("Op de goede plek: %s" % bp)
                        print("Niet op de goede plek, maar wel in de geheime code: %s" % wp)
                        print("Poging: ", count)
                        if bp == 4:
                            print("Correct!")
                            break

        if __name__ == "__main__":
            g = Game()
            g.main()
    main()

if choise ==  2: ###https://www.python-course.eu/mastermind.php
    def make_code():
        code = input("Voer een geheime code in (bijvoorbeeld rgbo): ")
        print("Geheime code:", code)
        return code

    def inconsistent(p, guesses):
        for guess in guesses:
            res = check(guess[0], p)
            (rightly_positioned, permutated) = guess[1]
            if res != [rightly_positioned, permutated]:
                return True  # inconsistent
        return False  # i.e. consistent


    def answer_ok(a):
        (rightly_positioned, permutated) = a
        if (rightly_positioned + permutated > number_of_positions) \
                or (rightly_positioned + permutated < len(colours) - number_of_positions):
            return False
        if rightly_positioned == 3 and permutated == 1:
            return False
        return True


    def get_evaluation():
        show_current_guess(new_guess[0])
        rightly_positioned = int(input("Blacks: "))
        permutated = int(input("Whites: "))
        return (rightly_positioned, permutated)


    def new_evaluation(current_colour_choices):
        rightly_positioned, permutated = get_evaluation()
        if rightly_positioned == number_of_positions:
            return (current_colour_choices, (rightly_positioned, permutated))

        if not answer_ok((rightly_positioned, permutated)):
            print("Input Error: Sorry, the input makes no sense")
            return (current_colour_choices, (-1, permutated))
        guesses.append((current_colour_choices, (rightly_positioned, permutated)))

        current_colour_choices = create_new_guess()
        if not current_colour_choices:
            return (current_colour_choices, (-1, permutated))
        return (current_colour_choices, (rightly_positioned, permutated))


    def check(p1, p2):
        blacks = 0
        whites = 0
        for i in range(len(p1)):
            if p1[i] == p2[i]:
                blacks += 1
            else:
                if p1[i] in p2:
                    whites += 1
        return [blacks, whites]


    def create_new_guess():
        next_choice = next(permutation_iterator)
        while inconsistent(next_choice, guesses):
            try:
                next_choice = next(permutation_iterator)
            except StopIteration:
                print("Error: Your answers were inconsistent!")
                return ()
        return next_choice


    def show_current_guess(new_guess):
        print("New Guess: ", end=" ")
        for c in new_guess:
            print(c, end=" ")
        print()


    if __name__ == "__main__":
        make_code()
        colours = ["r", "g", "b", "o", "p", "z"]
        guesses = []
        number_of_positions = 4

        permutation_iterator = all_colours(colours, number_of_positions)
        current_colour_choices = next(permutation_iterator)

        new_guess = (current_colour_choices, (0, 0))
        while (new_guess[1][0] == -1) or (new_guess[1][0] != number_of_positions):
            new_guess = new_evaluation(new_guess[0])
