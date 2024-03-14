def find_triad(note1):
    note2 = (note1 + 2) % 7
    note3 = (note2 + 2) % 7
    return note2, note3

if __name__ == '__main__':
    note1 = int(input('The first note:'))

    note2, note3 = find_triad(note1)

    scale = 'CDEFGAB'
    print('Triad: ', str(note1), str(note2), str(note3))
    print(scale[note1-1]+','+scale[note2-1]+','+scale[note3-1])