def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

main()
    

