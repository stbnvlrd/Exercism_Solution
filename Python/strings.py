def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    mod_word = "un"+word

    return mod_word


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    mod_word = vocab_words[0]
    i=1
    while i < len(vocab_words):
        mod_word = mod_word + ' :: ' + vocab_words[0] + vocab_words[i]
        i += 1
    return mod_word


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    if "iness" in word:
        new_word = word.replace("iness", "y")
    else:
        new_word = word.replace("ness", "")
    print(new_word)
    return new_word


def adjective_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    new_sentence = sentence.replace(".", "")
    split_sentence = new_sentence.split()
    new_verb = split_sentence[index] + "en"
    
    print(new_verb)
    return new_verb
