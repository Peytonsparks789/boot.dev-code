def find_total_words(contents):
    return len(contents.split())

def find_total_character_counts(contents):
    char_set = {}
    contents = contents.lower()
    for char in contents:
        if char in char_set:
            char_set[char] = char_set[char] + 1
        else:
            char_set[char] = 1

    return char_set

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    sorted_chars = []

    for key, value in char_dict.items():
        sorted_chars.append({"char": key, "num": value})

    sorted_chars.sort(key=sort_on, reverse=True)

    return sorted_chars
