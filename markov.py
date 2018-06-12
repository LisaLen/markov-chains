"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()

    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()

    chains = {}
    for i in range(len(words)-2):       
       
        words_key = (words[i], words[i+1])

        add_word = words[i+2]

        if words_key in chains:
            chains[words_key].append(add_word)
        else:
            chains[words_key] = [add_word]

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    keys_lst  = list(chains.keys())
    link_tpl = choice(keys_lst)
    words.extend(list(link_tpl))

    while link_tpl in chains:
        link_word_str = choice(chains[link_tpl])
        words.append(link_word_str)
        link_tpl = (link_tpl[1], link_word_str)



    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
