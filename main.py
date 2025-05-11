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
    print(get_book_text("./books/frankenstein.txt"))




main()    

