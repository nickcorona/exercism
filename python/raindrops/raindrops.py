def raindrops(number):
    words = []
    if number % 3 == 0:
        words.append('Pling')
    if number % 5 == 0:
        words.append('Plang')
    if number % 7 == 0:
        words.append('Plong')

    if len(words) == 0:
        return str(number)
    else:
        return ''.join(words)
