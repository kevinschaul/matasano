# Expected frequencies via WikiPedia:
# https://en.wikipedia.org/wiki/Letter_frequency
expected_frequencies = {
    'a': .08167,
    'b': .01492,
    'c': .02782,
    'd': .04253,
    'e': .13000,
    'f': .02228,
    'g': .02015,
    'h': .06094,
    'i': .06966,
    'j': .00153,
    'k': .00772,
    'l': .04025,
    'm': .02406,
    'n': .06749,
    'o': .07507,
    'p': .01929,
    'q': .00095,
    'r': .05987,
    's': .06327,
    't': .09056,
    'u': .02758,
    'v': .00978,
    'w': .02360,
    'x': .00150,
    'y': .01974,
    'z': .00074,
    ' ': .14000,
}

def score(plaintext_bytes):
    """
    Attempts to score a string based on closeness to expected English
    letter frequencies.

    Scores range from 0 to 1, with 1 being a perfect match to the expected
    frequencies.
    """
    plaintext = plaintext_bytes.decode('ascii')
    plaintextLength = len(plaintext)
    letters = [letter.lower() for letter in plaintext if isEnglishCharacter(letter)]
    lettersLength = len(letters)
    counts = {}
    for letter in letters:
        count = counts.get(letter, 0)
        counts[letter] = count + 1

    difference = 0
    frequencies = {}
    for letter in counts:
        count = counts.get(letter)
        expected = expected_frequencies.get(letter, 0) * lettersLength
        difference += abs(count - expected)

    if lettersLength == 0:
        differencePerLetter = 1
    else:
        differencePerLetter = difference / lettersLength

    if plaintextLength == 0:
        percentLetters = 0
    else:
        percentLetters = lettersLength / plaintextLength

    # differencePerLetter should be close to 0
    # percentLetters should be close to 1
    return abs(1 - differencePerLetter) * percentLetters

def isEnglishCharacter(c):
    """
    Returns whether the character is generally used in English writing.
    """
    return True
    if c.isalpha() or c in [' ', '\t', '\n', '.', ',', '?', '!', ';', ':',
            '\'', '"', '/', '\\', '(', ')', '[', ']', '#', '$', '%', '&', '-',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False

