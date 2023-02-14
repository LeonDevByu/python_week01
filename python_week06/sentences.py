# 06 Prove Assignment: Troubleshooting Functions
# NAME: EDWIN LEONARDO LEON MATIAS

import random


def main():
    # single past
    word_01 = get_determiner(1)
    word_02 = get_noun(1)
    word_03 = get_verb(1, "past")
    word_04 = get_preposition()  # empty
    word_05 = get_prepositional_phrase(1)  # word_01
    word_06 = get_noun(1)  # word_02
    word_07 = get_adjective()
    print(f"a. {word_01} {word_02} {word_03} {word_04} {word_05} {word_06} {word_07}")

    # single present
    word_01 = get_determiner(1)
    word_02 = get_noun(1)
    word_03 = get_verb(1, "present")
    word_04 = get_preposition()  # empty
    word_05 = get_prepositional_phrase(1)  # word_01
    word_06 = get_noun(1)  # word_02
    word_07 = get_adjective()
    print(f"b. {word_01} {word_02} {word_03} {word_04} {word_05} {word_06} {word_07}")

    # single future
    word_01 = get_determiner(1)
    word_02 = get_noun(1)
    word_03 = get_verb(3, "future")
    word_04 = get_preposition()  # empty
    word_05 = get_prepositional_phrase(1)  # word_01
    word_06 = get_noun(1)  # word_02
    word_07 = get_adjective()
    print(f"c. {word_01} {word_02} {word_03} {word_04} {word_05} {word_06} {word_07}")

    # plural past
    word_01 = get_determiner(2)
    word_02 = get_noun(2)
    word_03 = get_verb(1, "past")
    word_04 = get_preposition()  # empty
    word_05 = get_prepositional_phrase(2)  # word_01
    word_06 = get_noun(2)  # word_02
    word_07 = get_adjective()
    print(f"d. {word_01} {word_02} {word_03} {word_04} {word_05} {word_06} {word_07}")

    # plural present
    word_01 = get_determiner(2)
    word_02 = get_noun(2)
    word_03 = get_verb(2, "present")
    word_04 = get_preposition()  # empty
    word_05 = get_prepositional_phrase(2)  # word_01
    word_06 = get_noun(2)  # word_02
    word_07 = get_adjective()
    print(f"e. {word_01} {word_02} {word_03} {word_04} {word_05} {word_06} {word_07}")

    # plural future
    word_01 = get_determiner(2)
    word_02 = get_noun(2)
    word_03 = get_verb(3, "future")
    word_04 = get_preposition()  # empty
    word_05 = get_prepositional_phrase(2)  # word_01
    word_06 = get_noun(2)  # word_02
    word_07 = get_adjective()
    print(f"f. {word_01} {word_02} {word_03} {word_04} {word_05} {word_06} {word_07}")


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

        # Randomly choose and return a noun.
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

        # Randomly choose and return a verb.
    word = random.choice(words)
    return word


def get_preposition():
    words = ["about", "above", "across", "after", "along",
             "around", "at", "before", "behind", "below",
             "beyond", "by", "despite", "except", "for",
             "from", "in", "into", "near", "of",
             "off", "on", "onto", "out", "over",
             "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a prepositional_phrase.
    word = random.choice(words)
    return word


def get_adjective():
    words = ["angry", "bad", "beautiful", "cheap", "clean", "cool", "cruel",
             "dirty", "false", "fat", "feeble", "good", "handsome", "happy",
             "hard", "heavy", "high", "hot", "long", "new", "old", "quick"]

    # Randomly choose and return a adjective.
    word = random.choice(words)
    return word


main()
