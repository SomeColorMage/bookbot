import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main(target_file):
    book = get_book_text(target_file)
    word_count = get_word_count(book)
    char_count = sort_char_count(get_char_count(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {target_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])