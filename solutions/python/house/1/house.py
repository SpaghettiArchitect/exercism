def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the nursery rhyme 'This is the House that Jack Built'
    from start_verse to end_verse (inclusive).

    Args:
        start_verse (int): The starting verse number (1-indexed).
        end_verse (int): The ending verse number (1-indexed).

    Returns:
        list[str]: A list of verses from start_verse to end_verse.
    """

    SENTENCE_PARTS = [
        ("house that Jack built", "lay in"),
        ("malt", "ate"),
        ("rat", "killed"),
        ("cat", "worried"),
        ("dog", "tossed"),
        ("cow with the crumpled horn", "milked"),
        ("maiden all forlorn", "kissed"),
        ("man all tattered and torn", "married"),
        ("priest all shaven and shorn", "woke"),
        ("rooster that crowed in the morn", "kept"),
        ("farmer sowing his corn", "belonged to"),
        ("horse and the hound and the horn", ""),
    ]

    rhyme = []
    for verse_number in range(start_verse, end_verse + 1):
        current_verse = SENTENCE_PARTS[:verse_number]
        noun = current_verse[-1][0]

        verse = (
            f"This is the {noun}"
            + "".join(
                [
                    f" that {verb} the {noun}"
                    for noun, verb in reversed(current_verse[:-1])
                ]
            )
            + "."
        )

        rhyme.append(verse)

    return rhyme
