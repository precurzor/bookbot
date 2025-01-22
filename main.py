def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    sorted_char = char_sorted_list(char_count)

    print(f"--- Begin report of {book_path} --- ")
    print(f"Total word count: {word_count}")
    print("") 
    for item in sorted_char:
        char = item['char']
        num = item['num']
        if char.isalpha():
            print(f"'{char}' appears {num} times") 

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

def sort_chars(char_count):
    return char_count['num']

def char_sorted_list(char_count):
    sorted_list = []
    for char, num in char_count.items():
        # Append dict that contains character and count
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_chars)
    return sorted_list

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