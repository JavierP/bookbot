import sys
from stats import get_book_text, word_counter, text_to_character, sort_on
def main():
    if len(sys.argv) == 2:
        book = get_book_text(sys.argv[1])
        wrd_cntr = word_counter(book)  
        ch = text_to_character(book)
        
        print("============ BOOKBOT ============")
        if book:
            print(f"Analyzing book found at {sys.argv[1]}...")
        if wrd_cntr:
            print("----------- Word Count ----------")
            print(wrd_cntr)
        ch.sort(reverse=True, key=sort_on)
        for key in range(0, len(ch)):
            print(f"{ch[key]["char"]}: {ch[key]["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()