def sort_on(dict):
    return dict["num"]

def count_words(book_text):
    """
    Args:
        book_text (str): text from book
    Returns:
        int: number of words in the string
    """
    word_list = book_text.split()
    num_words = len(word_list)
    print(f"Found {num_words} total words")
    return num_words

def count_chars(book_text):
    """
    Args:
        book_text (str): text from book
    Returns:
        dict: char-->count 
    """
    chars = {}


    for c in book_text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_dict(char_dict):
    """
    Args:
        dict: char-->int to be sorted
    Returns:
        list of dicts: e.g. {"char": "b", "num": 4868}
    """
    char_list = []
    for char in char_dict:
        if char.isalpha():
            key = char
            val = char_dict[char]
            char_new = {"char": f"{key}", "num": val}
            char_list.append(char_new)

    char_list.sort(reverse=True, key=sort_on)
    return char_list





