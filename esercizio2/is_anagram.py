
def is_anagram(a, b):
    return sorted(a.strip().lower()) == sorted(b.strip().lower())
