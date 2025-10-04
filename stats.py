def num_of_words(text):
    words = len(text.split())
    return f"Found {words} total words"

def character_count(text):
    char_count = {}
    for c in text:
        c = c.lower()
        count = char_count.get(c, 0)
        char_count[c] = count + 1
    return char_count