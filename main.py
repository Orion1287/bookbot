from stats import text_from_book
import sys
from stats import repitition_in_book
from stats import sorting
from stats import sorton
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents





def main():
    #import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]  # This gets the first argument after the script name    text = get_book_text("./books/frankenstein.txt")
    text = get_book_text(path)
    print(text)
    number = text_from_book(text)
    print(number)
    repition = repitition_in_book(text)
    print(repition)
    sorted_chars = sorton(repition)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")


main()

