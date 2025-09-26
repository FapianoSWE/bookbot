from stats import get_word_count_from_book
from stats import get_character_occurance
from stats import get_sorted_character_occurance
from sys import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents










def main():
    if len(argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_file_path = argv[1]
    book_text = get_book_text(book_file_path)
    word_count = get_word_count_from_book(book_text)
    character_occurance = get_character_occurance(book_text)
    sorted_list = get_sorted_character_occurance(character_occurance)
    
    print("============ BOOKBOT ============")
    print(F"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(F"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(F"{dict["char"]}: {dict["num"]}" )
    print("============= END ===============")
main()