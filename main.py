def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words

from stats import get_letter_count

from stats import sorted_dict

def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = count_words(text)
    letter_count = get_letter_count(text)
    sorted_list = sorted_dict(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_data in sorted_list:
        print(f"{char_data["char"]}: {char_data["num"]}")
    print("============= END ===============")
    

main()
    

