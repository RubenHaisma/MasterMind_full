import itertools
import collections
import random
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

    def random_secret(): ###https://stackoverflow.com/questions/33240666/word-guessing-game-what-algorithm-to-use
        return [random.randrange(COLORS) for _ in range(PEGS)]

    def all_states():
        return list(itertools.product(*[range(COLORS) for _ in range(PEGS)]))

    def evaluate(secret, guess):
        color_and_pos = 0
        color = 0
        colors = collections.defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                color_and_pos += 1
            else:
                colors[secret[i]] += 1
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                if colors[guess[i]] > 0:
                    colors[guess[i]] -= 1
                    color += 1
        return (color_and_pos, color)

    def list_count(l):
        #for python >= 2.7 you can use collections.Counter
        return dict((x, l.count(x)) for x in set(l))

    def dict_max_value(d):
        return max(d.values())

    def minmax(fun, actions):
        min, choice = None, None
        for action in actions:
            max = fun(action)
            if choice is None:
                min, choice = max, action
            elif max <= min:
                min, choice = max, action
        return choice

    class Algo():
        def __init__(self):
            self.contenders = all_states()
        def initial_guess(self):
            return tuple([0] * int(PEGS/2) + [1] * int(PEGS - PEGS/2))
        def next_guess(self, qnas):
            self.filter_contenders(qnas[-1])
            #print "contenders size: ", len(self.contenders)
            return minmax(lambda candidate:
                dict_max_value(list_count(
                  [evaluate(contender, candidate) for contender in self.contenders]
                )), self.contenders)

        def filter_contenders(self, qna):
            self.contenders = [contender for contender in self.contenders
                                         if evaluate(contender, qna[0]) == qna[1]]

    class Game():
        def __init__(self, algo):
            self.algo = algo
        def run(self):
            secret = random_secret()
            print("Secret:", secret)
            qnas = []
            n = 1
            guess = self.algo.initial_guess()
            while True:
                answer = evaluate(secret, guess)
                qnas.append((guess, answer))
                print(guess, "->", answer)
                if answer == (PEGS, 0):
                    break
                guess = self.algo.next_guess(qnas)
                n += 1
            print("Done in", n, "steps")

    Game(Algo()).run()