import random
import itertools
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

if choise == 2:
    COLORS, PEGS = 6, 4
    def all_states():  ###https://stackoverflow.com/questions/33240666/word-guessing-game-what-algorithm-to-use
        lst = list(itertools.product(*[range(COLORS) for _ in range(PEGS)]))
        return lst

    def convert_lst(): #algoritme maken
        lst = all_states()
        new_lst = [tuple(s if s != 0 else 'r' for s in tup) for tup in lst]
        new_lst_1 = [tuple(s if s != 1 else 'g' for s in tup) for tup in new_lst]
        new_list_2 = [tuple(s if s != 2 else 'b' for s in tup) for tup in new_lst_1]
        new_list_3 = [tuple(s if s != 3 else 'o' for s in tup) for tup in new_list_2]
        new_list_4 = [tuple(s if s != 4 else 'p' for s in tup) for tup in new_list_3]
        possibilities = [tuple(s if s != 5 else 'z' for s in tup) for tup in new_list_4]
        return possibilities

    def random_secret():
        code = input("Bedenk een geheime code (bijvoorbeeld: rrbb): ")
        return code

    def random_guess():
        possibilities = convert_lst()
        guess = random.choice(possibilities)
        print("Gok van de computer: ", guess)
        return guess

    def check_first():
        guess = random_guess()
        code = random_secret()
        if guess == code:
            print("De computer raadde je code in 1x!")
        else:
            print("Gok van de computer: ", guess)
        return code

    def create_new_guess():
        code = random_secret()
        colours = ['r', 'g', 'b', 'o', 'p', 'z']
        guess = random_guess()
        first_chac = guess[0]
        print("Geiheme code: ", code)
        blacks = int(input("Hoe veel op de goede plaats: "))
        whites = int(input("Hoe veel niet op de goede plaats, maar wel in de geheime code: "))
        if blacks == 4:
            print("Computer heeft gewonnen!")
        if blacks == 3:
            new_code = (first_chac * 3) + random.choice(colours)
            if new_code == code:
                print("Succes!")
                print(new_code)
            else:
                create_new_guess()
        if blacks == 2:
            print("cool")
            new_code_2 = (first_chac * 2) + 2*random.choice(colours)
            if new_code_2 == code:
                print("Succes!")
                print(new_code_2)
            else:
                create_new_guess()
        if blacks == 1:
            new_code_1 = (first_chac * 1) + 3*random.choice(colours)
            if new_code_1 == code:
                print("Succes!")
                print(new_code_1)
            else:
                create_new_guess()
        if blacks == 0:
            random_guess()
        else:
            print("Computer wins!")
        '''while blacks <4:
            if blacks == 3:
                new_code = (first_chac * 3) + (random.choice(colours))
                print(new_code)
                create_new_guess()
            if blacks == 2:
                new_code = (first_chac * 2) + (2 * random.choice(colours))
                print(new_code)
                create_new_guess()
            if blacks == 1:
                new_code = (first_chac) + (3 * random.choice(colours))
                print(new_code)
                create_new_guess()
            if blacks == 0:
                new_code = random.choice(lines)
                print(new_code)
                create_new_guess()'''

    random_secret()
    random_guess()
    check_first()
    create_new_guess()
