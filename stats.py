def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    char_dict = {}
    for char in book.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_count(count):
    sorted_list = []
    for item in list(count):
        sorted_list.append({
            "char": item,
            "num": count[item]
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list