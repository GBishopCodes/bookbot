from stats import get_books_text
from stats import get_characters
from stats import sort_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
   #DEBUG print(f"{get_books_text(sys.argv[1])} words found in the document")
   #DEBUG print(f"{get_characters(sys.argv[1])}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------")
    print(f"Found {get_books_text(sys.argv[1])} total words")
    print("--------- Character Count -------")
    temp = sort_characters(get_characters(sys.argv[1]))
    for temps in temp:
        print(f'{temps["char"]}: {temps["num"]}')
    print("============= END ===============")
main()