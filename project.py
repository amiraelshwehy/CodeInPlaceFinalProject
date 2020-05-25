import pprint
import enchant
from helpers import filter_symbols

def main():
    file_name = input("Enter file name to spell check: ")  # Get file name from user
    file = open(file_name)  # Open file
    lines = file.read().splitlines()  # Split file into lines

    line_number = 0  # The current line number we are processing (the index of the dict)
    words_count = 0  # Number of all words in line
    incorrect_words = {}  # A dictionary of incorrect words in file

    for line in lines:  # For every line in file
        words = line.split()  # Split lines into words
        line = filter_symbols(line) # Filter line from symbols
        words_count += len(words)  # Keep count of words in file
        line_number += 1  # Keep count of line number
        result = get_incorrect_words_in_line(line)  # Add a list of incorrect words in current line of file to dictionary
        if result:
            incorrect_words[line_number] = result

    print_statistics(incorrect_words, words_count)  # Print spell check statistics


def print_statistics(incorrect_words, words_count):
    incorrect_words_count = 0  # Number of incorrect words in line
    for value in incorrect_words.values():
        incorrect_words_count += len(value)  # Keep count of incorrect words in current line
    incorrect_words_perc = (incorrect_words_count * 100) // words_count  # Calculates percentage of incorrect words in file

    print("words count = " + str(words_count))
    print("Incorrect words count = " + str(incorrect_words_count))
    print("percentage of incorrect words = " + str(incorrect_words_perc) + "%")
    user_answer = input("Do you want a list of incorrect words? y/n: ")
    if len(user_answer) == 0 or user_answer == "y":
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(incorrect_words)
    else:
        print("Thanks!")


def get_incorrect_words_in_line(line,):  # Returns a list of incorrect words in line (if any)
    words = line.split()  # Split lines into words
    incorrect_words_in_line = []    # An empty list to keep track of incorrect words in line

    for word in words:  # For every word in line
        if not spell_check_word(word):  # If spell checked word returns false "ie: word is incorrect"
            incorrect_words_in_line.append(word)  # Add incorrect word to a list of incorrect words in line
    return incorrect_words_in_line


def spell_check_word(word):  # Returns False if word is incorrect
    d = enchant.Dict("en_US")  # Set dictionary language to English
    return d.check(word)  # Check for incorrect words


if __name__ == "__main__":
    main()
