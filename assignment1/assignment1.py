# Task 1: Hello

def hello():
    return "Hello!"


# Task 2: Greet with a Formatted String

def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator

def calc(arg_1, arg_2, operation="multiply"):
    try:
        match operation:
            case "multiply":
                return arg_1 * arg_2
            case "add":
                return arg_1 + arg_2
            case "subtract":
                return arg_1 - arg_2
            case "divide":
                return arg_1 / arg_2
            case "modulo":
                return arg_1 % arg_2
            case "int_divide":
                return arg_1 // arg_2    
            case "power":
                return arg_1 ** arg_2     
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    

# Task 4: Data Type Conversion

def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return float(value)
            case "int":
                return int(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
# Task 5: Grading System, Using *args

def grade(*args):
    try:
        grade_average = sum(args) / len(args)
        if grade_average >= 90:
            return "A"
        elif grade_average >= 80:
            return "B"
        elif grade_average >= 70:
            return "C"
        elif grade_average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
    

# Task 6: Use a For Loop with a Range

def repeat(string, count):
    new_string = ""
    for i in range(count):
        new_string += string
    return new_string


# Task 7: Student Scores, Using **kwargs

def student_scores(mode, **kwargs):
    if not kwargs:
        return None
    
    if mode == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif mode == "mean":
        average_score = sum(kwargs.values()) / len(kwargs)
        return average_score
    
    return None


# Task 8: Titleize, with String and List Operations

def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            words[i] = word.capitalize()
            
    joined_words = " ".join(words)
    return joined_words
   

# Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    result = ""
    
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
   
   
# Task 10: Pig Latin, Another String Manipulation Exercise

def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        first_vowel_index = len(word)
        for i, letter in enumerate(word):
            is_qu = letter == "u" and i > 0 and word[i - 1] == "q"
            if letter in vowels and not is_qu:
                first_vowel_index = i
                break
        pig_latin_words.append(word[first_vowel_index:] + word[:first_vowel_index] + "ay")

    return " ".join(pig_latin_words)