def main():
    book_path = "books/frankenstein.txt"
    
    with open(book_path) as f:
        file_contents = f.read()
        print(file_contents)

main()