def perf_note(pnotes, coefficient):
    for note in pnotes:
        if note[1] <= coefficient <= note[2]:
            return note[0]
    return "Note not found"  # This can be adjusted based on your specific needs

if __name__ == "__main__":
    pnotes = [['head note', 1, 14],
              ['heart note', 15, 60],
              ['base note', 61, 100]]

    note = perf_note(pnotes, 8)
    print(note)

    note = perf_note(pnotes, 34)
    print(note)

    note = perf_note(pnotes, 78)
    print(note)
