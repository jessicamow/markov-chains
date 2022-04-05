"""Generate Markov text from text files."""

import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path)
    data = text_file.read().replace('\n', ' ')
    text_file.close()    
    # print(data)

    return data


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
    key = ()    
    value = []
    string_list = text_string.split()
    for i in range(len(string_list)-2):            
        key = (string_list[i], string_list[i+1])
                
        if key in chains:
            chains[key].append(string_list[i+2])
        else:
            chains[key] = [string_list[i+2]]   
    # print(chains)
    

    return chains

current_key = ()

def make_text(chains):
    """Return text from chains."""

    words = []

    # Get a random key as the first link for our text output
    first_link = random.choice(list(chains.keys()))
    
    # words.append(first_link[0]) !!!!
    
    # print(first_link)
    # Add the words in that key to the text output
    # Pull out a random word from that key's values list
    # Create a new key using the key[1] and the random word
    # Check to see if the new key exists in the dictionary
    # If it does, repeat the process
    current_key = first_link

    while current_key in chains.keys():
        # current_key = key
        
        # chosen_word = chains[key][0]
        # chosen_word = key[1]
        chosen_word = random.choice(chains[current_key])

        # new_key = (current_key[1], chosen_word) 
        # print("=================>" + str(new_key))
        words.append(current_key[0])
        # words.append(chosen_word)
        current_key = (current_key[1], chosen_word)
    # print(words)
    words.append(current_key[0])
    words.append(current_key[1])
    
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
