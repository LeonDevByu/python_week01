# 05 Prove Milestone: Testing and Fixing Functions
# NAME: EDWIN LEONARDO LEON MATIAS

import random


def main():
    # single past
    word01 = get_determiner(1)
    word02 = get_noun(1)
    word03 = get_verb(1, "past")
    print(f"a. {word01} {word02} {word03}")

    # single present
    word01 = get_determiner(1)
    word02 = get_noun(1)
    word03 = get_verb(1, "present")
    print(f"b. {word01} {word02} {word03}")

    # single future
    word01 = get_determiner(1)
    word02 = get_noun(1)
    word03 = get_verb(3, "future")
    print(f"c. {word01} {word02} {word03}")

    # plural past
    word01 = get_determiner(2)
    word02 = get_noun(2)
    word03 = get_verb(1, "past")
    print(f"d. {word01} {word02} {word03}")

    # plural present
    word01 = get_determiner(2)
    word02 = get_noun(2)
    word03 = get_verb(2, "present")
    print(f"e. {word01} {word02} {word03}")

    # plural future
    word01 = get_determiner(2)
    word02 = get_noun(2)
    word03 = get_verb(3, "future")
    print(f"f. {word01} {word02} {word03}")


def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]

        # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    if tense == "past" and quantity == 1:
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

        # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


main()
