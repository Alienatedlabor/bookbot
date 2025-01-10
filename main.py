#wrap auxillary functions
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_book_words(text)
    character_dict = count_book_characters(text)
    create_book_report(word_count, character_dict)

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
         
    return character_dict  

def create_book_report(word_count, character_dict):
    dict_list = []
    def sort_on(dict_list):
      return dict_list["num"]
   
    

    #iterate through dictionary by key and value, append key and value to list if key is alphabetic. https://www.programiz.com/python-programming/methods/built-in/iter
    for key, value in iter(character_dict.items()):
        if key.isalpha() == True:
            dict_list.append({"char": key, "num": value})
      
 
    dict_list.sort(reverse=True, key=sort_on)
    for entry in dict_list:
       print(f"The '{entry['char']}' character was found {entry['num']} times")

    print(f"The book has {word_count} words")


#call entry-point function
main()