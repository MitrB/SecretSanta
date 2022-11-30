import random, sys

SEED = 1

def make_random_pairs(names, seed=SEED):
    random.seed(seed)
    random.shuffle(names)
    names_copy = names.copy()

    last = names_copy.pop()
    names_copy = [last] + names_copy

    pairs = list(zip(names, names_copy))

    return pairs


if __name__ == "__main__":
    args = sys.argv

    names_filename = "names.txt"

    # set seed
    for i, a in enumerate(args):
        if a == "-s":
            SEED = args[i+1]
        elif a == "-n":
            names_filename = args[i+1]

    print(f"Creating pairs with seed: {SEED}")
    if SEED == 1:
        print(f"Change seed with -s flag")

    names = []
    try:
        with open(names_filename, "r") as names_file:
            names = [line[:-1] for line in names_file]
    except (FileNotFoundError):
        print(f"ERROR: File not found: {names_filename}")
        print("Use -f flag to define your names file.")
        exit(1)
    
    pairs = make_random_pairs(names)
    
    # Shuffle pairs so they are not in order of giver -> taker
    random.shuffle(pairs)

    for pair in pairs:
        with open(pair[0], "w") as file:
            file.write(f"{pair[0]} gives to {pair[1]}\n")
