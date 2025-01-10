#wrap auxillary functions
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_book_words(text)

# find book path and return entire text
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count words in entire text after splitting string by whitespace, print word count
def count_book_words(text):
    word_count = 0
    words = text.split()

    for word in words:
      word_count += 1
    print(f"The book has {word_count} words")
    return word_count

#call entry-point function
main()