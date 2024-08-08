"""
Objectives:

Open the file - DONE
Clean the input - DONE

Set up a maps with one and two words as keys - DONE

Pick a random word:
    -> This will involve counting syllables as well. If something is larger than the limit, we can call recursively to pick another random word
    -> This will also need to return the number of syllables as that is something we need to keep track of. If we want the first line to be five, 
       then we need to know what the first word's value is. 

Pick the next word in the haiku:
    -> Using the word we previously picked as a key, we can randomly pick from the associated values
    -> There is an edge case to handle, what if our key has no values associated?
        -> I think we would want to just pick another random key and keep it moving but will need to test

Functions to build the Haiku:
    -> Since we want the user to be able to regenerate lines two and three, it might be better to containerize them.
        -> Set up a function for the first line, the second line, and third line. 
            -> If the user wants to redo them, it will be as simple as a function call for the specific line. 
        -> We also want to keep track of the end of the previous line, since we'll still need to randomly choose that from the values.
            -> This might be a little more difficult than I initially thought. If a user wants to regen line 2, but not line 3, how do we
               keep line 3 the same without updating the "next word"?
    -> We need to keep track of the current line we're building as well. Best to do this with an array. It will also make printing them much easier later
       down the road. 
        -> It will be something like this end_of_line = prev_line[-2:]

Setting up the user interface:
    -> I'm not exactly sure how I want to do this right now. It could be as simple as some sort of REPL setup. 
    -> We could give the user specific commands that trigger function calls. That seems like the easiest way, but I am unsure. 
        




"""



import sys
import logging
import random
import pprint
from collections import defaultdict
from count_syllables import count_syllables


def open_file(file):
    with open(file) as f:
        raw_words = f.read()
    
    return raw_words

def clean_words(raw_words):
    processed_words = raw_words.replace("\n", " ").split()

    return processed_words

def map_one_word(processed_words):

    max_idx = len(processed_words) - 1
    one_word_map = defaultdict(list)

    for i, word in enumerate(processed_words):
        if i < max_idx:
            one_word_map[word] = processed_words[i + 1]
    
    return one_word_map

def map_two_words(processed_words):
    max_idx = len(processed_words) - 2
    two_word_map = defaultdict(list)

    for i, word in enumerate(processed_words):
        if i < max_idx:
            two_word_map[word + " " + processed_words[i + 1]] = processed_words[i + 2]
    
    return two_word_map



def main():

    raw_words = open_file('train.txt')
    processed_words = clean_words(raw_words)
    one_word_map = map_one_word(processed_words)
    map_two_words(processed_words)
    

main()