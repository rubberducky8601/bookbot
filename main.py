from stats import count_words, count_chars, sort_dict

def sort_on(dict):
    return dict["num"]

def get_book_text(filepath):
    """
    Args:
       filepath (str): path to book 

    Returns:
        str: full book as str
    """
    with open(filepath) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")

    text = get_book_text("./books/frankenstein.txt")

    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")

    count_words(text)

    print("--------- Character Count -------")
    char_dict = count_chars(text) 

    sorted_char_list = sort_dict(char_dict)

    for char in sorted_char_list:
        print(f"{char['char']}: {char['num']}")

    print("============= END ===============")





main()

