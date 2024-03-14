def rational_decision(s, p):
    not_confess = 0
    confess = 0
    not_confess_outcome = s[p][0]
    confess_outcome = s[p][1]

    for i in range(0, len(confess_outcome)):
        if not_confess_outcome[i] > confess_outcome[i]:
            confess += 1
        elif not_confess_outcome[i] < confess_outcome[i]:
            not_confess = not_confess + 1

    if not_confess > confess:
        return 0
    elif not_confess < confess:
        return 1
    else:
        return None





if __name__ == '__main__':
    choices = ['not confess', 'confess']
    s = {'Lobha': [[3, 10], [1, 5]], 'Raga': [[3, 10], [1, 5]]}
    p = 'Lobha'
    r = rational_decision(s, p)
    print(p, ':', choices[r])