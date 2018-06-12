So I'll admit I got a little stuck here:
```
KeyError: '-'
```
I couldn't figure out why it was passing the simple test data but not the dictionary file itself.

So that was the point I looked for the review post that mentioned this
error and reminded me thatsome words in the English language have
hyphens, and it mentioned theKeyError. So that was kind of an "Aha!"
moment so I changed
```Python
word_value += LETTER_SCORES[char.upper]
```
to
```Python
word_value += LETTER_SCORES.get(char.upper(), 0)
```

I also made some unnecessary intermediates in my ```max_word_value``` function
```Python
def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    word_values = {word: calc_word_value(word) for word in words}
    max_word_pair = max(word_values.items(), key=lambda word_val: word_val[1])

    max_word = max_word_pair[0]
    return max_word
```

Compare to experienced coder Bob Belderbos's version:
```Python
def max_word_value(words=None):
    return max(words or load_words(), key=lambda w: calc_word_value(w))
```

Also I am still coming to terms with git/github/venv/using GitHub with
PyCharm/navigating Bob and Julian's web sites and differing versions of
the instructions. I actually spent more time with those aspects on it
than the Python, but it was time well spent.

-DE



