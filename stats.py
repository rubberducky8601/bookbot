def count_words(book_text):
    """
    Args:
        book_text (str): text from book
    Returns:
        int: number of words in the string
    """
    word_list = book_text.split()
    num_words = len(word_list)
    print(f"{num_words} words found in the document")
    return num_words
