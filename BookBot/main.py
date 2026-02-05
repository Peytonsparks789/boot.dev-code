import sys
from stats import find_total_words
from stats import find_total_character_counts
from stats import sort_char_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main(file_path):
    book_contents = get_book_text(file_path)
    print(f"Found {find_total_words(book_contents)} total words")
    
    char_counts = find_total_character_counts(book_contents)

    for i in sort_char_dict(char_counts):
        print(f"{i["char"]}: {i["num"]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])
