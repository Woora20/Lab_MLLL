def read_codons(fname):
    d = {}
    with open(fname, 'r') as f:
        for line in f:
            k, v = line.split('=')
            if v[-1] == '\n':
                v = v[:-1]
            d[k] = v

    return d

def codon(codon_table, gene):
    cod_tab = read_codons(codon_table)

    # Read DNA sequence first
    dna = ""
    with open(gene, "r")as f:
        for line in f:
            line = line.replace("\n", "")
            dna += line[1:]  # Skip the first character (URL indicator)

    # Translate each 3-letter set in DNA sequence to an amino acid
    polypep = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon in cod_tab:
            amino_acid = cod_tab[codon]
            polypep.append(amino_acid)
            if amino_acid == 'stop':
                break  # Stop translation if 'stop' codon is encountered

    return polypep

if __name__ == '__main__':
    res = codon('codons.txt', 'homo_sapiens_mitochondrion.txt')
    print(res)
    print(len(res))
