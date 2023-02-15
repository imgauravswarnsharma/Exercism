def distance(strand_a, strand_b):
    count = 0
    if len(strand_a)!= len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for char in range(len(strand_a)):
        if strand_a[char] != strand_b[char]:
            count +=1
    return count