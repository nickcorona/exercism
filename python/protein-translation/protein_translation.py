codon_protein_dict = {
    "AUG": ["Methionine"],
    "UUU": ["Phenylalanine"],
    "UUC": ["Phenylalanine"],
    "UUA": ["Leucine"],
    "UUG": ["Leucine"],
    "UCU": ["Serine"],
    "UCC": ["Serine"],
    "UCA": ["Serine"],
    "UCG": ["Serine"],
    "UAU": ["Tyrosine"],
    "UAC": ["Tyrosine"],
    "UGU": ["Cysteine"],
    "UGC": ["Cysteine"],
    "UGG": ["Tryptophan"],
    "UAA": ["STOP"],
    "UAG": ["STOP"],
    "UGA": ["STOP"],
}


def proteins(strand):
    if len(strand) % 3 != 0:
        return []

    proteins = []
    for i in range(0, len(strand), 3):
        proteins += codon_protein_dict[strand[i: i + 3]]
        if "STOP" in proteins:
            break
    return proteins 

proteins('AUGUCG')

# for i in range(0, len('AUGACC'), 3):
#     print('AUGACC'[i: i + 3])


# Codon                 | Protein
# :---                  | :---
# AUG                   | Methionine
# UUU, UUC              | Phenylalanine
# UUA, UUG              | Leucine
# UCU, UCC, UCA, UCG    | Serine
# UAU, UAC              | Tyrosine
# UGU, UGC              | Cysteine
# UGG                   | Tryptophan
# UAA, UAG, UGA         | STOP
