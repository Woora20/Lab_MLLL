def count_kmer(substring, text):
    count = 0
    start_index = 0
    
    while start_index < len(text):
        index = text.find(substring, start_index)
        
        if index != -1:
            start_index = index + 1
            count += 1
        else:
            break
    
    return count

if __name__ == "__main__":
    result = count_kmer('ACTAT', 'ACAACTATGCATACTATCGGGAACTATC')
    print(result)
    
    result = count_kmer('AC', 'ACAACTATGCATACTATCGGGAACTATC')
    print(result)
    
    result = count_kmer('ATA', 'CGATATATCCATAG')
    print(result)
