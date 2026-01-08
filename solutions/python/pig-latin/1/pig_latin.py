def translate(text: str) -> str:
    """Translate a text to Pig Latin."""
    translated_text = []
    for word in text.split(" "):
        translated_text.append(translate_word(word))

    return " ".join(translated_text)


def translate_word(word: str) -> str:
    """Translate a single word to Pig Latin."""
    vowels = ("a", "e", "i", "o", "u")

    # If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to
    #   the end of the word.
    if word.startswith((*vowels, "xr", "yt")):
        return word + "ay"

    # If a word begins with one or more consonants, first move those consonants to the
    #   end of the word and then add an "ay" sound to the end of the word.
    starting_consonants = ""
    rest_of_word = ""
    for i, char in enumerate(word):
        if char not in vowels:
            # If a word starts with one or more consonants followed by "y", first move
            #   the consonants preceding the "y" to the end of the word, and then add an
            #   "ay" sound to the end of the word.
            if char == "y" and starting_consonants:
                break
            starting_consonants += char
        else:
            # If a word starts with zero or more consonants followed by "qu", first move
            #   those consonants (if any) and the "qu" part to the end of the word, and
            #   then add an "ay" sound to the end of the word.
            if char == "u" and starting_consonants[-1] == "q":
                starting_consonants += char
                i += 1
            break

    rest_of_word = word[i:]

    return rest_of_word + starting_consonants + "ay"
