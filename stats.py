def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_letter_count(text):
    alpha_dict = {}
    lowercase = text.lower()
    for letter in lowercase:
        if letter not in alpha_dict:
            alpha_dict[letter] = 1
        else:
            alpha_dict[letter] += 1
    return alpha_dict

def sort_on(text):
    return text["num"]

def sorted_dict(char_counts):
    sorted_list = []
    for char in char_counts:
        current_char = char
        count = char_counts[char]
        if char.isalpha() == True:
            temp_dict = {"char" : current_char, "num" : count}
            sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list