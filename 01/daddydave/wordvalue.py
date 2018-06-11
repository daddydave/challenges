from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY) as dictionary_file:
        for line in dictionary_file:
            words.append(line.rstrip())
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for char in word:
        word_value += LETTER_SCORES.get(char.upper(), 0)
    return word_value


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    word_values = {word: calc_word_value(word) for word in words}
    max_word_pair = max(word_values.items(), key=lambda word_val: word_val[1])

    max_word = max_word_pair[0]
    return max_word


if __name__ == "__main__":
    pass  # run unittests to validate
