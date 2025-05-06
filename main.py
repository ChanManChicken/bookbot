from stats import count_words, character_counter
import sys

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


def main():
    # Check if the correct number of command line arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # sys.argv is command line argument
    book = sys.argv[1]

    text = get_book_text(book)
    word_count = count_words(text)
    character_count = character_counter(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for characters in character_count:
        if characters.isalpha():
            print(f"{characters}: {character_count[characters]}")
    print("============= END ===============")
    
main()