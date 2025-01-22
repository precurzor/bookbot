def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)

    print(f"Reading {book_path}")
    print(f"Word Count = {word_count}")

def count_words(file_contents):
    words = file_contents.split()  
    return len(words)

main()