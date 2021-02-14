import random
import itertools
import time

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
        global possibilities
        lst = all_states()
        new_lst = [tuple(s if s != 0 else 'r' for s in tup) for tup in lst]
        new_lst_1 = [tuple(s if s != 1 else 'g' for s in tup) for tup in new_lst]
        new_list_2 = [tuple(s if s != 2 else 'b' for s in tup) for tup in new_lst_1]
        new_list_3 = [tuple(s if s != 3 else 'o' for s in tup) for tup in new_list_2]
        new_list_4 = [tuple(s if s != 4 else 'p' for s in tup) for tup in new_list_3]
        possibilities = [tuple(s if s != 5 else 'z' for s in tup) for tup in new_list_4]
        return possibilities

    def random_secret():
        global code
        code = input("Bedenk een geheime code (bijvoorbeeld: rrbb): ")
        return code

    def random_guess():
        global guess, lines
        lines = open("mastermind_final.txt").read().splitlines()
        guess = random.choice(lines)
        print("Gok van de computer: ", guess)
        return guess

    '''def minmax(fun, actions):
        min, choice = None, None
        for action in actions:
            max = fun(action)
            if choice is None:
                min, choice = max, action
            elif max <= min:
                min, choice = max, action
        return choice

    def create_random():
        count = 0
        while True:
            new_code = random.choice(lines)
            if new_code == code:
                print(new_code)
                print("Code geraden in: ",count, "pogingen")
                break
            else:
                count +=1'''

    def give_return():
        global blacks, whites
        blacks = int(input("Hoe veel op de goede plaats: "))
        whites = int(input("Hoe veel niet op de goede plaats, maar wel in de geheime code: "))
        return blacks, whites


    def create_new_guess():
        infile = "mastermind_final.txt"
        outfile = "new_textfile.txt"
        count = 1
        colours = ['r', 'g', 'b', 'o', 'p', 'z']
        while blacks < 4:
            if blacks == 3:
                new_code = random.choice(colours) + (3*random.choice(guess))
                print(lines)
                print(new_code)
                count +=1
            elif blacks == 2:
                new_code = (2*random.choice(colours)) + (2*random.choice(guess))
                print(new_code)
                count +=1
            elif blacks == 1:
                new_code = (3*random.choice(colours)) + random.choice(guess)
                print(new_code)
                count += 1
            elif blacks == 0:
                new_code = random.choice(lines)
                print(new_code)
                count += 1
            else:
                print("Computer wint!", count, "stappen")
                break
            with open(infile) as fin, open(outfile, 'w') as fout:
                for line in fin:
                    for guess in lines:
                        line = line.replace(guess, "")
                    fout.write(line)

            give_return()


    random_secret()
    random_guess()
    give_return()
    create_new_guess()

    '''if black == 3 
            chose 1new colour + 3 random from code
        if black == 2:
            chose 2 new colour from colours + 2 random from code
        if black == 1:
            chose 1 new colour from colours + 2 random from code'''
    
