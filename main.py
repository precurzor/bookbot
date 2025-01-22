def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)

    print(f"Reading {book_path}")
    print(f"Word count = {word_count}")
    print(f"Character count = {char_count}")

def count_words(file_contents):
    words = file_contents.split()  
    return len(words)

def count_chars(file_contents):
    char_dict = {}
    lower_string = file_contents.lower()
    for char in lower_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict   

# I DID TOO MUCH! Thought it was only a to z...
# def count_chars(file_contents):
    # char_dict = {}
    # lower_string = file_contents.lower()
    # lower_string_no_space = "".join(lower_string.split())
    # for char in lower_string_no_space:
        # if 'a' <= char <= 'z':
            # if char in char_dict:
                # char_dict[char] += 1
            # else:
                # char_dict[char] = 1
    # return char_dict        

main()