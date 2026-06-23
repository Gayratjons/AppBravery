###############################################################################################################################################################################
# Only write your code within the area mentioned below.
# Implement the functions corresponding to their names.
# You are not allowed to change the function names nor the name of the parameter.
# Return your student ID in the first function
###############################################################################################################################################################################
def your_ID():
    return "12245023"


def isVowel(letter):
    try:
        # Write your code here########################
        vowels = "eioau"
        return letter in vowels
        ##############################################
    except Exception:
        return None


def isEven(num):
    try:
        # Write your code here########################
        return num % 2 == 0
        ##############################################
    except Exception:
        return None


def Tri_check_validity(a, b, c):
    try:
        # Write your code here########################
        return a + b > c and a + c > b and b + c > a
        ##############################################
    except Exception:
        return None


def leapyearCheck(year):
    try:
        # Write your code here########################
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        ##############################################
    except Exception:
        return None


def calc_tax(income):
    try:
        # Write your code here########################
        # tax_inp = 150000
        tax = 0
        if income <= 50000:
            tax += tax_inp * 0.05
        elif income <= 150000 and income > 50000:
            tax = 2500
            tax += (income - 50000) * 0.1
        elif income > 150000:
            tax = 12500
            tax += (income - 150000) * 0.15
        return tax
        ##############################################
    except Exception:
        return None


def lowest_number(a, b, c, d, e):
    try:
        # Write your code here########################
        numbers = [a, b, c, d, e]
        negaive_count = 0
        for i in numbers:
            if i > -1:
                chosen = i
                break
            else:
                chosen = 0
        for i in numbers:
            if i < 0:
                negaive_count += 1
            if i < chosen and i > -1:
                chosen = i
        if negaive_count == len(numbers):
            return 0
        else:
            return chosen
        ##############################################
    except Exception:
        return None


def count_vowels(word):
    try:
        # Write your code here########################
        vowels = 'euioa'
        count = 0
        for i in word:
            if i in vowels:
                count += 1
        return count
        ##############################################
    except Exception:
        return None


def greet_people(lst):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def hamming_distance(string1, string2):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def filter_list(lst):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def count(lst):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def unique_sort(lst):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def correct_stream(user, correct):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def find_odd(lst):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def sum_odd_and_even(*num):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def list_of_multiples(num, length):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def majority_vote(votes):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def atbash(text):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


def tic_tac_toe(board):
    try:
        # Write your code here########################
        return NotImplemented
        ##############################################
    except Exception:
        return "Error"


###############################################################################################################################################################################

###############################################################################################################################################################################
# Do not Modify this section
###############################################################################################################################################################################
def main(x):
    try:
        if x == 0: return your_ID(), isVowel('a'), isEven(10), Tri_check_validity(7, 10, 5), leapyearCheck(
            12), calc_tax(250000), lowest_number(12, 3, 5, 18, 20), count_vowels("Celebration"), greet_people(
            ["Joe"]), hamming_distance("abcde", "bcdef"), filter_list([1, 2, "a", "b", 1]), count(
            [5, 9, 10, 3, "J", "A", 4, 8, 5]), unique_sort([1, 2, 4, 3]), correct_stream(["it", "is", "find"],
                                                                                         ["it", "is",
                                                                                          "fine"]), find_odd(
            [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), sum_odd_and_even(1, 2, 3, 4, 5, 6), list_of_multiples(7,
                                                                                                         5), majority_vote(
            ["A", "A", "B"]), atbash("apple"), tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]])
        if x == 1: return your_ID(), isVowel('b'), isEven(7), Tri_check_validity(3, 9, 5), leapyearCheck(100), calc_tax(
            40000), lowest_number(100, 15, -5, 4, 3), count_vowels("Palm"), greet_people(
            ["Angela", "Joe"]), hamming_distance("abcde", "abcde"), filter_list([1, "a", "b", 0, 15]), count(
            ["A", "A", "K", "Q", "Q", "J"]), unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]), correct_stream(
            ["april", "showrs", "bring", "may", "flowers"], ["april", "showers", "bring", "may", "flowers"]), find_odd(
            [20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), sum_odd_and_even(-1, -2, -3, -4, -5, -6), list_of_multiples(12,
                                                                                                                    10), majority_vote(
            ["A", "A", "A", "B", "C", "A"]), atbash("Hello world!"), tic_tac_toe(
            [["O", "O", "O"], ["O", "X", "X"], ["E", "X", "X"]])
        if x == 2: return your_ID(), isVowel('e'), isEven(16), Tri_check_validity(15, 10, 11), leapyearCheck(
            2024), calc_tax(125000), lowest_number(16, 8, 4, 11, 4), count_vowels("Prediction"), greet_people(
            ["Frank", "Angela", "Joe"]), hamming_distance("strong", "strung"), filter_list(
            [1, 2, "aasf", "1", "143", 123]), count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]), unique_sort(
            [6, 7, 3, 2, 1]), correct_stream(["cat", "blue", "skt", "umbrells", "paddy"],
                                             ["cat", "blue", "sky", "umbrella", "paddy"]), find_odd(
            [10]), sum_odd_and_even(0, 0), list_of_multiples(17, 6), majority_vote(
            ["A", "B", "B", "A", "C", "C"]), atbash("Christmas is the 25th of December"), tic_tac_toe(
            [["X", "X", "O"], ["O", "O", "X"], ["X", "X", "O"]])
        if x == 3: return your_ID(), isVowel('u'), isEven(109), Tri_check_validity(25, 10, 11), leapyearCheck(
            400), calc_tax(235000), lowest_number(26, 75, -21, 35, 75), count_vowels("University"), greet_people(
            ["Robert", "Chris", "Steven"]), hamming_distance("ParamountUniverse", "panasoundunicurse"), filter_list(
            [1, 2, 3, 4, 5, "6", "7", "8", "9", "10"]), count(["A", 5, "J", 2, 6, 2, 3, 10, 9, 7, "Q"]), unique_sort(
            [11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13]), correct_stream(["ezy", "fell", "gren", "scy"],
                                                                                  ["easy", "fall", "green",
                                                                                   "sky"]), find_odd(
            [20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5, 20, 4]), sum_odd_and_even(1, 2, 3, -3, -2, -4, 12, 13, 14, 15,
                                                                                100, 101), list_of_multiples(3,
                                                                                                             21), majority_vote(
            ["A", "B", "B", "B", "C"]), atbash("abcdefg"), tic_tac_toe(
            [["X", "X", "X"], ["O", "O", "X"], ["E", "O", "X"]])
        if x == 4: return your_ID(), isVowel(''), isEven(0), Tri_check_validity(2, 1, 1), leapyearCheck(2040), calc_tax(
            195000), lowest_number(2, 7, -2, -5, -7), count_vowels("AeIoUUUUUioUtrf"), greet_people(
            ["Robert Downey", "Chris Evans", "Steven Gerrard"]), hamming_distance("ParamountUniverse",
                                                                                  "panasoundunicurse"), filter_list(
            [1, 2, 3, 4, 5, "6", "7", "8", "9", "10"]), count(["A", 5, "J", 2, 6, 2, 3, 10, 9, 7, "Q"]), unique_sort(
            [11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13]), correct_stream(["ezy", "fell", "gren", "scy"],
                                                                                  ["easy", "fall", "green",
                                                                                   "sky"]), find_odd(
            [20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5, 20, 4]), sum_odd_and_even(10, 20, 31, -13, -12, -14, 101, 130, 14,
                                                                                15, 100, 101), list_of_multiples(9,
                                                                                                                 25), majority_vote(
            ["A", "A", "A", "A", "B", "B"]), atbash("Programming Practice"), tic_tac_toe(
            [["O", "X", "O"], ["X", "O", "X"], ["X", "O", "X"]])
    except:
        return "Error"


###############################################################################################################################################################################

for i in range(5):
    print(main(i))