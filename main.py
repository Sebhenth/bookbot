def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("/Users/james/Daniel/projects/bookbot/books/frankenstein.txt")
    book_text_list = book_text.split()
    num_words = len(book_text_list)
    print(f"Found {num_words} total words")
                    


main()
