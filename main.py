import sys
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

from stats import num_of_words 

from stats import character_count

from stats import mk_dict_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------""")
    print(num_of_words(get_book_text(sys.argv[1])))
    print("--------- Character Count -------")
    char_count_dictionary = character_count(get_book_text(sys.argv[1]))
    final_dictlist = mk_dict_list(char_count_dictionary)
    for dict in final_dictlist:
        if dict["char"].isalpha():
            a = dict["char"]
            b = dict["num"]
            print(f"{a}: {b}")
        else:
            continue
    print("============= END ===============")

main()