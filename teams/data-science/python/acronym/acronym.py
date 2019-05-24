import pdb
import re

regex = re.compile(
    "[^a-zA-Z -]"
)  # used to remove all characters that aren't spaces, letters, or hyphens


def abbreviate(words):
    cleaned_words_lst = regex.sub("", words).replace("-", " ").split()
    return "".join([word[0].capitalize() for word in cleaned_words_lst])
