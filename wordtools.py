import re


def has_dashdash(string):
    if string.find("--") < 0:
        return False
    else:
        return True


def cleanword(string):
    string = re.sub("[^a-zA-Z0-9]", "", string)
    return string


def extract_words(string):
    string_group = string.lower()
    string_group = re.split("[^a-z0-9]", string_group)
    return list(filter(lambda x: x != "", string_group))


def wordcount(string, group):
    count = 0
    for word in group:
        if word == string:
            count += 1
    return count


def wordset(string_group):
    extract_duplicates = list(set(string_group))
    extract_duplicates.sort()
    return extract_duplicates


def longestword(group):
    max_size = 0
    for word in group:
        if max_size < len(word):
            max_size = len(word)
    return max_size
