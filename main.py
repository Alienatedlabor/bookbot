#wrap auxillary functions
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_book_words(text)
    count_book_characters(text)

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

# count the number of times each character appears in the string.
def count_book_characters(text):
    character_dict = {}
    lowered_string = text.lower()

# loop through each character, add character to dict if not there, if there increment int value.
    for character in lowered_string:
      if character not in character_dict:
        character_dict[character] = 1
      else: 
         character_dict[character] += 1
         
    print(character_dict)
    return character_dict  




#call entry-point function
main()