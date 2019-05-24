def raindrops(number):
    factors = (3, 5, 7)
    sounds = ("Pling", "Plang", "Plong")
    strings = []

    for factor, sound in zip(factors, sounds):
        if number % factor == 0:
            strings.append(sound)
    return "".join(strings) or str(number)
