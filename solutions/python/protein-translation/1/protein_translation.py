def proteins(strand: str) -> str:
    """Convert an RNA strand into a list of proteins. Translation stops if a stop
    codon is encountered.

    Args:
        strand (str): The RNA strand to be translated.

    Returns:
        str: A list of proteins translated from the RNA strand.
    """
    codon_to_amino_acid = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
    }

    proteins_found = []
    for i in range(0, len(strand) - 1, 3):
        codon = strand[i : i + 3]
        if codon in ["UAA", "UAG", "UGA"]:
            break
        proteins_found.append(codon_to_amino_acid[codon])

    return proteins_found
