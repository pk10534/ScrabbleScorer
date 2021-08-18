
#Dictionary with number as key, list of letters as value
OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

#Take parameter (word), turn upper case, declares empty var named LetterPoints. For each char in word, and for the point value in the word inputed Old Scrabble scorer>
# If the char in OSS (key = point value), letterpoints is equal "points for the char in word: value of the point." Add together
#Return letterpoints statement
def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   word_entry = input("Enter a word to score: ")
   return word_entry


def simple_scorer(word):
    word = word.upper()
    letterpoints = ""
    letterpoints += 'Points for {word}: {point_value}\n'.format(word = word, point_value = (len(word)))

    return letterpoints

def vowel_bonus_scorer(word):
    word = word.upper()
    letterpoints = ""
    num_vowels = 0
    num_consanants = 0
    
    for char in word:
        if char in 'AEIOU':
            num_vowels += 1
    vowel_points = num_vowels * 3
    for char in word:
        if char not in 'AEIOU':
            num_consanants +=1
    
    total_points = vowel_points + num_consanants
    letterpoints = 'Points for {word}: {total_points}\n'.format(word = word, total_points = total_points)

    
    return letterpoints

def scrabble_scorer(word):
    score = 0
    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]
    return score

simple_scorer_dict = {'name': 'Simple Scorer', 'descrption' : 'Each letter is worth one point', 'scoring_function' : simple_scorer}
vowel_bonus_dict = {'name' : 'Bonus Vowels', 'description': 'Vowels are 3pts, consonants are 1pt', 'scoring_function' : vowel_bonus_scorer}
original_scrabble_dict = {'name' : 'Scrabble', 'description' : 'The traditional scoring algorithm', 'scoring_function' : scrabble_scorer}


scoring_algorithms = (simple_scorer_dict, vowel_bonus_dict, original_scrabble_dict)


def scorer_prompt():
    init_algorithm_choice = input("Choose your scorer: \n0 for simple scrabble scoring\n1 for vowel bonus\n2 for the original scrabble method\nEnter Here: ")
    algorithm_choice = int(init_algorithm_choice)
    return algorithm_choice


def transform(new_dictionary):
    new_dict = {}
    new_dict["' '"] = 0
    for (key, value) in new_dictionary.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict

new_point_structure = transform(OLD_POINT_STRUCTURE)


def run_program():
    word = initial_prompt()
    selected_dict = scorer_prompt()
    score = scoring_algorithms[selected_dict]['scoring_function']

    print('Algorithm name: ', scoring_algorithms[selected_dict]['name'])
    result = score(word)
    print(result)
    # print('Total score for word "' , word, '":' , result)
    



    
    





    # word = initial_prompt()
    # scoring_choice = scorer_prompt()
    # print("Algorithm Name: ", scoring_algorithms[0]['name'])
    # score_function = scoring_algorithms[0]['score_function0']
    # print(score_function(word))


    #old point scorer
    # word = initial_prompt()
    # print(old_scrabble_scorer(word))

    #simple scorer
    # word = simple_scorer("hello")
    # print(word)

    #vowel combo points
    # word = vowel_bonus_scorer("hello")
    # print(word)
    
    
    
    
    