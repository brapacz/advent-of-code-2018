doublets = 0
triplets = 0
both = 0

def have_amount_of_chars(word, amount):
    for char in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
        if word.count(char) == amount:
            return True
    return False


for line in open("inputs/day-02.txt", "r"):
    line = line.rstrip()
    have_doubles = have_amount_of_chars(line, 2)
    have_triples = have_amount_of_chars(line, 3)
    # if have_doubles and have_triples:
    #     both += 1
    if have_doubles:
        doublets += 1
    if have_triples:
        triplets += 1

print(doublets * triplets)
