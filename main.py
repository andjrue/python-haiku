"""
Objectives:

Open the file - DONE
Clean the input - DONE

Set up a maps with one word keys - DONE

Pick a random word:
    -> This will involve counting syllables as well. If something is larger than the limit, we can call recursively to pick another random word
    -> This will also need to return the number of syllables as that is something we need to keep track of. If we want the first line to be five, 
       then we need to know what the first word's value is. 

** DONE **

Pick the next word in the haiku:
    -> Using the word we previously picked as a key, we can randomly pick from the associated values
    -> There is an edge case to handle, what if our key has no values associated?
        -> I think we would want to just pick another random key and keep it moving but will need to test

** DONE **

Functions to build the Haiku:
    -> Since we want the user to be able to regenerate lines two and three, it might be better to containerize them.
        -> Set up a function for the first line, the second line, and third line. 
            -> If the user wants to redo them, it will be as simple as a function call for the specific line. 
        -> We also want to keep track of the end of the previous line, since we'll still need to randomly choose that from the values.
            -> This might be a little more difficult than I initially thought. If a user wants to regen line 2, but not line 3, how do we
               keep line 3 the same without updating the "next word"?

** DONE ** -> This mostly went according to plan but got out of hand very quickly. What a mess!

Setting up the user interface:
    -> I'm not exactly sure how I want to do this right now. It could be as simple as some sort of REPL setup. 
    -> We could give the user specific commands that trigger function calls. That seems like the easiest way, but I am unsure. 

** DONE ** This was as simple as using a while loop. I'll probably pretty it up a bit more though. 
        

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
            one_word_map[word].append(processed_words[i + 1])
    
    return one_word_map

def map_two_words(processed_words):
    max_idx = len(processed_words) - 2
    two_word_map = defaultdict(list)

    for index, word in enumerate(processed_words):
        if index < max_idx:
            key = word + ' ' + processed_words[index + 1]
            suffix = processed_words[index + 2]
            two_word_map[key].append(suffix)
    
    return two_word_map

def pick_random_word(processed_words):
    first_word = random.choice(processed_words)
    word_syllables = count_syllables(first_word)

    if word_syllables > 4:
        pick_random_word(processed_words)
    else:
        return(first_word, word_syllables)

def build_first_line(first_word, first_word_syllables, one_word_map):
    # print("Building First Line")
    first_line = []
    target = 5
    total_syllables = first_word_syllables
    first_line.append(first_word)
    next_word = first_word
    #print("First word values: ", one_word_map.get(next_word))

    while total_syllables < target:
        if next_word in one_word_map:
            key = random.choice(one_word_map[next_word])
            syllables = count_syllables(key)
            
            if total_syllables + syllables > target:
                # print(f"Total Syllables + Syllables exceeds target: ", total_syllables)
                # print(f"Skipping Word: {key} (> than {target})")
                continue
            
            total_syllables += syllables
            first_line.append(key)
            next_word = key


            if total_syllables == target:
                # print(f"Total Syllables == Target: ", total_syllables)
                break
        else:
            key = random.choice(list(one_word_map.keys()))
            syllables = count_syllables(key)
            next_word = key


   
    # print(first_line)
    
    # We are going to return the last word and use it as an argument for our next line
    last_word = first_line[-1]
    last_word_syllables = count_syllables(last_word)
    #print("Last Word: ", last_word)
    # print(first_line)
    return first_line, last_word, last_word_syllables

def build_second_line(last_word, one_word_map, two_word_map, first_line):
    # print("Building Second Line")
    second_line = []
    target = 7
    total_syllables = 0
    next_word = first_line[-2] + " " + first_line[-1]

    # print("Line 2 initial syll check: ",total_syllables)
    while total_syllables < target:
        # print(total_syllables) - Adding syllables each time, even if the word does work. Sigh. 
        if next_word in two_word_map:
            key = random.choice(two_word_map[next_word])
            syllables = count_syllables(key)
            # print(syllables)
            
            if total_syllables + syllables > target:
                # print("Stuck at second line")
                continue
                # This isn't prety, but I think it will fix the loop
            
            total_syllables += syllables
            second_line.append(key)
            next_word = key


            if total_syllables == target:
                # print(f"Total Syllables == Target: ", total_syllables)
                break

        else:

            next_word = random.choice(list(one_word_map.keys()))
            syllables = count_syllables(next_word)
            if total_syllables + syllables <= target:

                total_syllables += syllables
                second_line.append(next_word)

    last_word = second_line[-1]
    last_word_syllables = count_syllables(last_word)
    #print(second_line)
    #print(total_syllables)
    return second_line, last_word, last_word_syllables

def build_third_line(last_word, one_word_map, two_word_map, second_line):
    #print("Building Third Line")
    third_line = []
    target = 5
    total_syllables = 0
    next_word = second_line[-2] + " " + second_line[-1]

    #print("Line 3 initial syll check: ",total_syllables)
    while total_syllables < target:
        # print(total_syllables) - Adding syllables each time, even if the word does work. Sigh. 
        if next_word in two_word_map:
            key = random.choice(two_word_map[next_word])
            syllables = count_syllables(key)
            #print(syllables)
            
            if total_syllables + syllables > target:
                #print("Stuck at third line")
                continue
            
            total_syllables += syllables
            third_line.append(key)
            next_word = key


            if total_syllables == target:
                # print(f"Total Syllables == Target: ", total_syllables)
                break

        else:

            next_word = random.choice(list(one_word_map.keys()))
            syllables = count_syllables(next_word)
            if total_syllables + syllables <= target:

                total_syllables += syllables
                third_line.append(next_word)

    last_word = third_line[-1]
    last_word_syllables = count_syllables(last_word)
    #print(third_line)
    #print(total_syllables)
    return third_line

def print_haiku(haiku):
    print("\n")
    for line in haiku:
        print(" ".join(line))

def main():

    raw_words = open_file('train.txt')
    processed_words = clean_words(raw_words)

    one_word_map = map_one_word(processed_words)
    two_word_map = map_two_words(processed_words)
    
    first_word, first_word_syllables = pick_random_word(processed_words) # We can use this word as our first key later down the road

    first_line, first_line_last_word, first_line_last_word_syllables = build_first_line(first_word, first_word_syllables, one_word_map)
    second_line, second_line_last_word, second_line_last_word_syllables = build_second_line(first_line_last_word, one_word_map, two_word_map, first_line)
    third_line = build_third_line(second_line_last_word, one_word_map, two_word_map, second_line)
    
    haiku = [first_line, second_line, third_line] 
    print("\n\nPrinting Haiku...")
    print_haiku(haiku)

    print("\nI hope you enjoyed your Haiku. Please see additional options below.\n" + "2 - Regenerate Line 2\n" + "3 - Regenerate Line 3\n" "4 - Exit the program\n")
    user_input = input("Please make a selection from the list above\n>> ")


    while True:
        if user_input == "2":
            second_line = []
            second_line, second_line_last_word, second_line_last_word_syllables = build_second_line(first_line_last_word, one_word_map, two_word_map, first_line)
            haiku[1] = second_line
            print_haiku(haiku)
            user_input = input("If you would like regenerate line 2, please enter 2. If you would like to regenerate line 3, please enter 3.\nIf you wish to exit the program, enter 4.\n >> ")
        elif user_input == "3":
            third_line = []
            third_line = build_third_line(second_line_last_word, one_word_map, two_word_map, second_line)
            haiku[2] = third_line
            print_haiku(haiku)
            user_input = input("If you would like to regenerate line 2, please enter 2. If you would like to regenerate line 3, please enter 3.\nIf you wish to exit the program, enter 4.\n >> ")
        elif user_input == "4":
            print("Thank you for using the Haiku Generator!")
            break
        else:
            print("Invalid input. Exiting the program.")
            break

"""
This should be working now. I ran it probably 50 times and didn't get caught in the loop I was worried about. I'm confident enough to say that it's working. 
I also haven't experienced the loop when regenerating the lines. 
"""

main()