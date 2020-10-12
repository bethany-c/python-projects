def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return(len(dna))
#print(get_length('ATCGAT'))

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return (len(dna1) > len(dna2))
#print(is_longer('ATCG', 'AT'))

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count = 0
    for letters in dna:
        if letters == nucleotide:
            count = count +1
    return count
#print(count_nucleotides('ATCGGC', 'G'))

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return (dna2 in dna1)
#print(contains_sequence('ATCGGC', 'GT'))

def is_valid_sequence(sequence):
    count = 0
    if len(sequence) == 0:
        return False
    for letters in sequence:
        if letters == 'A' or letters == 'C' or letters == 'G' or letters == 'T':
            continue
        else:
            count = count + 1
    return (count == 0)
#print(is_valid_sequence(''))

def insert_sequence(dna1, dna2, index):
    new = dna1[0:index] + dna2 + dna1[index:]
    return new
#print(insert_sequence('', 'AT', 2))
        
def get_complement(nucleotide):
    #checks for valid
    if(is_valid_sequence == False):
        return
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
#print(get_complement(''))

def get_complementary_sequence(sequence):
    #checks for valid
    if(is_valid_sequence == False):
        return
    complement = ''
    for letter in sequence:
        complement = complement + get_complement(letter)
    return complement

#print(get_complementary_sequence('ACTGCA'))
