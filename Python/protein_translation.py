def proteins(strand):
    codons = [""]*int(len(strand)/3)
    protein = []
    for index in range(len(strand)):
        codons[(index//3)] =  codons[(index//3)] + strand[index]
    for element in codons:
        if element == "AUG":
            protein.append("Methionine")
        elif element == "UUU" or element == "UUC":
            protein.append("Phenylalanine")
        elif element == "UUA" or element == "UUG":
            protein.append("Leucine")
        elif element == "UCU" or element == "UCC" or element == "UCA" or element == "UCG":
            protein.append("Serine")
        elif element == "UAU" or element == "UAC":
            protein.append("Tyrosine")
        elif element == "UGU" or element == "UGC":
            protein.append("Cysteine")
        elif element == "UGG":
            protein.append("Tryptophan")
        elif element == "UAA" or element == "UAG" or element == "UGA": 
            break
    return protein
