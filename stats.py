def get_book_text(filepath):
    file_contents = ""
    with open(f"{filepath}") as f:
        file_contents = f.read()
        return file_contents

def word_counter(file):
    num_words = len(file.split())
    return f"Found {num_words} total words"

def sort_on(items):
    return items["num"]

def text_to_character(file):
    result = {}
    result2 = []
    for ch in file:
        if ch.isalpha():
            low = ch.lower()
            if low not in result:
                result[low] = 0
            result[low] += 1
    for key in result:
        result2.append({"char": f"{key}", "num": result[key]})
    
    return result2

