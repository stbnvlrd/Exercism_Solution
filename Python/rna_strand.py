def to_rna(dna_strand):
    rna_strand = ""
    add_strand = ""
    for index in dna_strand:
        if index == "G": add_strand = "C"
        elif index == "C": add_strand = "G"
        elif index == "T": add_strand = "A"
        elif index == "A": add_strand = "U"
        rna_strand = rna_strand + add_strand
    return rna_strand