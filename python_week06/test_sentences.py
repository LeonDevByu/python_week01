# 06 Prove Milestone: Testing and Fixing Functions
# NAME: EDWIN LEONARDO LEON MATIAS

from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.
    single_determiners = ["a", "one", "the"]

    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    # 2. Test the plural determiners.
    plural_determiners = ["some", "many", "the"]

    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single noun.
    single_noun = ["bird", "boy", "car", "cat", "child",
                   "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        word = get_noun(1)
        assert word in single_noun

    # 2. Test the plural noun.
    plural_noun = ["birds", "boys", "cars", "cats", "children",
                   "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        word = get_noun(2)
        assert word in plural_noun


def test_get_verb():
    # 1. Test the single verb.
    single_verb_past = ["drank", "ate", "grew", "laughed", "thought",
                        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(1, "past")
        assert word in single_verb_past

    single_verb_present = ["drinks", "eats", "grows", "laughs", "thinks",
                           "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, "present")
        assert word in single_verb_present

    single_verb_future = ["will drink", "will eat", "will grow", "will laugh",
                          "will think", "will run", "will sleep", "will talk",
                          "will walk", "will write"]
    for _ in range(4):
        word = get_verb(3, "future")
        assert word in single_verb_future

    # 2. Test the plural verb.
    plural_verb_past = ["drank", "ate", "grew", "laughed", "thought",
                        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(1, "past")
        assert word in plural_verb_past

    plural_verb_present = ["drink", "eat", "grow", "laugh", "think",
                           "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2, "present")
        assert word in plural_verb_present

    plural_verb_future = ["will drink", "will eat", "will grow", "will laugh",
                          "will think", "will run", "will sleep", "will talk",
                          "will walk", "will write"]
    for _ in range(4):
        word = get_verb(3, "future")
        assert word in plural_verb_future


def test_get_preposition():
    # 1. Test the single preposition.
    single_preposition = ["about", "above", "across", "after", "along",
                          "around", "at", "before", "behind", "below",
                          "beyond", "by", "despite", "except", "for",
                          "from", "in", "into", "near", "of", "off",
                          "on", "onto", "out", "over", "past", "to",
                          "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()
        assert word in single_preposition

    # 2. Test the plural preposition.
    plural_preposition = ["about", "above", "across", "after", "along",
                          "around", "at", "before", "behind", "below",
                          "beyond", "by", "despite", "except", "for",
                          "from", "in", "into", "near", "of", "off",
                          "on", "onto", "out", "over", "past", "to",
                          "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()
        assert word in plural_preposition


def test_get_prepositional_phrase():
    # 1. Test the single prepositional_phrase.
    single_prepositional_phrase = ["a", "one", "the"]

    for _ in range(4):
        word = get_prepositional_phrase(1)
        assert word in single_prepositional_phrase

    # 2. Test the plural prepositional_phrase.
    plural_prepositional_phrase = ["some", "many", "the"]

    for _ in range(4):
        word = get_prepositional_phrase(2)
        assert word in plural_prepositional_phrase


def test_get_adjective():
    # 1. Test the single adjective.
    single_adjective = ["angry", "bad", "beautiful", "cheap", "clean", "cool", "cruel",
                        "dirty", "false", "fat", "feeble", "good", "handsome", "happy",
                        "hard", "heavy", "high", "hot", "long", "new", "old", "quick"]

    for _ in range(4):
        word = get_adjective()
        assert word in single_adjective

    # 2. Test the plural adjective.
    plural_adjective = ["angry", "bad", "beautiful", "cheap", "clean", "cool", "cruel",
                        "dirty", "false", "fat", "feeble", "good", "handsome", "happy",
                        "hard", "heavy", "high", "hot", "long", "new", "old", "quick"]

    for _ in range(4):
        word = get_adjective()
        assert word in plural_adjective


pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])
