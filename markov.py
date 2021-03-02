"""Generate Markov text from text files."""

#open file into a new variable
#make new empty string
#parse by word (not line) and add to a string
#concatenate with += to build a long string


from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    markov_file = open(file_path)
    long_string = ""
    for word in markov_file:
        seuss_word = word.rstrip()
        dr_seuss_word = seuss_word.strip(" ")
        long_string += dr_seuss_word + " "
    
    return long_string


#iterate through string
#go through pairs of 2 and assign as a tuple
#empty dictionary
#each tuple becomes the key in a dictionary
#the word after a pair of words is a value of the pairs key
#conditional to decide if that tuple is already in the dict 
    #if not, add to dict
    #if is, the dictionary is complete (break)

def make_chains(text_string):

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
