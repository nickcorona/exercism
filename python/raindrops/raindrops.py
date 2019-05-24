def raindrops(number):
    factors = (3, 5, 7)
    sounds = ("Pling", "Plang", "Plong")
    strings = [sound for factor, sound in zip(factors, sounds) if number % factor == 0]
    return "".join(strings) or str(number)
