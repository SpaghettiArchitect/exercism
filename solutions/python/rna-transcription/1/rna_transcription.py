def to_rna(dna_strand: str) -> str:
    """Transcribes a given DNA strand into its RNA complement.

    Args:
        dna_strand (str): A string representing the DNA strand.

    Returns:
        str: A string representing the transcribed RNA strand.
    """
    DNA_TO_RNA = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return "".join([DNA_TO_RNA[nucleotide] for nucleotide in dna_strand])
