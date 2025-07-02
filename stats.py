def get_books_text(filepath):
    total_words = 0
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read().split()
        for word_count in file_contents:
            total_words += 1
    return total_words

def get_characters(filepath):
    alphabet_dictionary = {}
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read().lower().split()
        file_contents = " ".join(file_contents)
        for character in file_contents:
            if character in alphabet_dictionary:
                alphabet_dictionary[character] += 1
            else:
                alphabet_dictionary[character] = 1
        return alphabet_dictionary
    
def sort_characters(dictionary):
    new_list = []
    for character in dictionary:
        if character in dictionary and character.isalpha():
            new_list.append({"char": character, "num": dictionary[character]})
    new_list.sort(key=lambda item: item["num"], reverse=True)
    return new_list

'''
My current plan is to take the text from the books and after counting each word join the list together as one massive block of words and iterate through the entire thing
to find every letter against the dictionary of letters. Hopefully this works.
'''