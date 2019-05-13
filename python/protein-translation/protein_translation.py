def proteins(strand):
    codons = []
    # split RNA into codons for easy lookup in dict
    for i in range(0, len(strand), 3):
        codons.append(strand[i : i + 3])

    proteins = []
    for codon in codons:
        if codon_dict()[codon] == "STOP":
            break
        proteins.append(codon_dict()[codon])
    return proteins


def codon_dict():
    return {
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
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }
