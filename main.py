def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

from stats import num_of_words 

from stats import character_count

def main():
    print(num_of_words(get_book_text("books/frankenstein.txt")))
    char_count_dictionary = character_count(get_book_text("books/frankenstein.txt"))
    print(char_count_dictionary)
main()