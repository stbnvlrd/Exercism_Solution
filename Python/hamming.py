def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) == len(strand_b):
        for x in range(len(strand_a)):
            if strand_a[x] != strand_b[x]:
                count += 1
    else:
        raise ValueError("Strands must be of equal length.")
    return count
