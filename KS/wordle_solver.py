# Import dictionary via csv as a Variable
#dictionary = importcsv as list

# Create variable for length of word we're looking for
class Word():

black_letters = []
green_letters = []
yellow_letters = []    

def __init__(self, length, chances):
    self.length = length
    self.chances = chances
    self.__initiate_list()

def __initiate_list(self):
    for letter in range(self.length):
        self.yellow_letters.append([])
        self.green_letters.append([])

def add_yellow(self, letter, position):
    self.yellow_letters[position-1].append(letter)

def add_green(self, letter, position):
    self.green_letters[position-1].append(letter)

def add_black(self, letter):
    self.black_letters.append(letter)

# Filter dictionary by: 
# i) Length of word, 
    #potential_words = [words for words in dictionary if len(words) == self.length]

# ii) filter out words with letters in black list
# ii) Each position of word using list of wrong letters (regex)

# Output should be list of possible words

# Create a function to add letters to any of the list

def wordle_solver(length, chances):
    wordle = Word(length, chances)

    for i in range(wordle.chances):
        word_guessed = input("Please input word guessed:")
        results = input("Please input the results of the word: (e.g. bbbyg)")
        if results == "ggggg":
            print("Congratulations!")
            return
        else:
            wordle_solver(length, chances) # this is an issue as it resets the wordle variable.
    


test_word = Word(5)
print(test_word.yellow_letters)
print(test_word.green_letters)

# Possible enhancements: 
# 1) web scrape dictionary
# 2) web scrape wordle to auto append letters to the list after guesses