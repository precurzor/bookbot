def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)

    print(f"Reading {book_path}")
    print(f"Word Count = {word_count}")

def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1    
    return count

main()