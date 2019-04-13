def hey(phrase):
    phrase = phrase.strip()
    if len(phrase) == 0:
        return "Fine. Be that way!"
    elif phrase[-1] == "?" and phrase.isupper():
        return "Calm down, I know what I'm doing!"
    elif phrase[-1] == "?":
        return "Sure."
    elif phrase.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
