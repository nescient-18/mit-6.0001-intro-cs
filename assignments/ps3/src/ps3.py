# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*' : 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "assignments/ps3/data/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)

    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """     
    return sum(SCRABBLE_LETTER_VALUES[c] for c in word.lower()) * \
           max(7 * len(word) - 3 * (n - len(word)), 1)

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print("Current Hand: ", end=" ")
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n, wild_count=1):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    wild_count: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={'*' : wild_count}  # start each hand with wildcard
    num_vowels = int(math.ceil(n / 3)) - wild_count  # make space for wildcard

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels+wild_count, n):  # since * counts as a vowel
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word_counts = get_frequency_dict(word.lower())
    return {c: max(hand[c] - word_counts.get(c, 0), 0) for c in hand}



#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """  
    word = word.strip().lower()  # handle stripping and lowering here to pass test cases, but is unnecessary for play_hand()
    word_counts = get_frequency_dict(word)

    # test hand has enough/appropriate letters
    for c in word_counts:
        if word_counts[c] > hand.get(c,0):  # if just one letter in `word` is 
            return False                    # more than what's available, return False    

    if word_counts.get('*', 0) > 0:  # slightly reduce runtime
        for v in VOWELS:  # go over all possible combinations
            if word.replace('*', v) in word_list:
                return True
        return False  # if none of the possibilities are valid, return false
    
    # check the longer operation last
    return word in word_list

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """

    hand_score = 0

    while calculate_handlen(hand) > 0:
        display_hand(hand)

        word = input('Enter word, or "!!" to indicate that you are finished: ').strip().lower()

        if word == '!!':
            break
        if is_valid_word(word, hand, word_list):
            word_score = get_word_score(word, HAND_SIZE)
            hand_score += word_score
            print(f'"{word}" earned {word_score} points. Total: {hand_score} points')
        else:
            print("That is not a valid word. Please choose another word.")
        hand = update_hand(hand, word)  # since update_hand() doesn't mutate list, neither does this line
        print()
    
    if word != '!!':
        print(f'Ran out of letters')

    return hand_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace ***all*** copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    if hand.get(letter,0) == 0:
        return hand
    
    new_hand = hand.copy()
    hand_letters = set(hand.keys())
    unique_letters = [c for c in string.ascii_lowercase if c not in hand_letters]  
    new_hand[random.choice(unique_letters)] = new_hand.pop(letter)

    return new_hand


       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    def get_hands():
        num_hands = input("Enter a total number of hands: ")

        while not num_hands.isnumeric():
            num_hands = input("Invalid input. Enter a total integer number of hands: ")
            print()
        
        return int(num_hands)
    
    def ask_yn(prompt):
        while True:
            r = input(prompt).strip().lower()
            if r in ('y', 'yes'):
                return True
            if r in ('n', 'no'):
                return False

    def get_sub(hand):
        sub = ask_yn('Would you like to substitute a letter? ')

        if sub:
            letter = input('Which letter would you like to replace? ').strip().lower()
            while not letter in SCRABBLE_LETTER_VALUES:
                letter = input('Which letter would you like to replace? ').strip().lower()
            print()
            return True, substitute_hand(hand, letter)
        print()
        return False, hand
    
    def do_replay(hand, hand_score):
        replay = ask_yn('Would you like to replay the hand? ')

        if replay:
            return True, max(hand_score, play_hand(hand, word_list))
        else:
            return False, hand_score

    num_hands = get_hands()
    sub = False
    replay = False
    total_score = 0

    for i in range(num_hands):
        # deal hand
        hand = deal_hand(HAND_SIZE)        

        # check if user wants sub
        if not sub:
            display_hand(hand)  # prevents from double display
            sub, hand = get_sub(hand)
        
        # play the hand, get hand score
        hand_score = play_hand(hand, word_list)

        # handle the ENTIRE process of replay, including checking for it and handling max score
        if not replay:
            replay, hand_score = do_replay(hand, hand_score)

        # tally score
        print(f'Total score for this hand: {hand_score}')
        print('----------')

        total_score += hand_score

    return total_score

        
   


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    score = play_game(word_list)
    print("Final score:", score)
