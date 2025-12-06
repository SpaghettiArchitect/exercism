def find_anagrams(word: str, candidates: list[str]):
    """Find all anagrams of 'word' in the list of 'candidates'.

    An anagram is a word formed by rearranging the letters of another,
    using all the original letters exactly once. The comparison is case-insensitive,
    and a word is not considered an anagram of itself.

    Args:
        word (str): The word to find anagrams for.
        candidates (list[str]): A list of candidate words to check against.

    Returns:
        list[str]: A list of anagrams found in the candidates.
    """
    word_low = word.lower()
    anagrams_found = []
    for candidate in candidates:
        candidate_low = candidate.lower()
        if word_low != candidate_low and sorted(word_low) == sorted(candidate_low):
            anagrams_found.append(candidate)

    return anagrams_found
