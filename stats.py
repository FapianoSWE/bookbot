from collections import Counter

def get_word_count_from_book(book_text : str):
    return len(book_text.split())

def get_character_occurance(book_text : str):
    lower_case_text = book_text.lower()
    character_dict = Counter(lower_case_text)
    return character_dict

def sort_on(items):
    return items["num"]

def get_sorted_character_occurance(occurance_counter):
    sorted_dict_list = []
    occurance_dict = dict(occurance_counter)
    for key,value in occurance_dict.items():
        if key.isalpha():
            sorted_dict_list.append({"char": key, "num": value})
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list
    