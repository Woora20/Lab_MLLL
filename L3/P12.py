import math

def clean_words(b):
    b = b.replace('\n', ' ')
    b = b.replace('.', ' ')
    b = b.replace('  ', ' ')

    b = b.lower()

    return b

def nice_print2Ddict(d):
    dkeys = list(d.keys())
    dkeys.sort()

    for k in dkeys:
        print('\n', k)

        d2 = d[k]
        k2s = list(d2.keys())
        k2s.sort()

        print('*', end=' ')
        for k2 in k2s:
            print("{}:{:.3f}".format(k2, d2[k2]), end='; ')

    print()


def culture_tf_idf(culture_list):

    ####################################################
    # Find f[t,d] ~ as a dictionary of dictionaries
    # dict (key=doc) of dict's (key=term)
    # List can be used too,
    # but dict seems to be more convenient.
    ####################################################

    Ftd = {}

    for c in culture_list:
        d = {}

        with open(c, 'r') as f:
            header = f.readline()
            msg = f.read()

            if header[-1] == '\n':
                header = header[:-1]

            msg = clean_words(msg)

            # print('header:', header)
            # print('msg:', msg)

            words = msg.split()
            for t in words:
                if t in d:
                    d[t] += 1
                else:
                    d[t] = 1

            # print('d = ', d)
            #
            Ftd[c] = d

    # print('Ftd = ', Ftd)

    ########################################################
    # IDF
    # * N
    # * Nt
    ########################################################

    ############
    # Find N
    ############
    N = len(Ftd) # number of documents
    # print('N = ', N)

    ########################################################
    # Count Nt
    # as dict (key=term)
    ########################################################
    Nt = {}
    for d in Ftd:
        term_freq = Ftd[d]
        for t in term_freq:
            if t in Nt:
                Nt[t] += 1
            else:
                Nt[t] = 1

    # print('Nt = ', Nt)

    ########################################################
    # Compute TF-IDF
    # Also dict (key=doc) of dict (key=term) is convenient
    ########################################################

    TF_IDF = {}
    for d in Ftd:
        term_freq = Ftd[d]

        # Find the TF denominator
        sum_all_ftd = 0
        for t in term_freq:
            sum_all_ftd += term_freq[t]

        # print(d, ': sum_all_ftd = ', sum_all_ftd)

        #########################
        # Calculate TF-IDF
        # Note: at this point
        # Ftd is ready
        # * Ftd[d][t] is accessing Ftd of doc d, term t
        # N, Nt are ready
        # * Nt[t] is accessing Nt of term t
        #########################
        tfidf_ = {}

        # Write your code here!!!

        # print('F[{}, {}] = '.format(d, t), Ftd[d][t])


        TF_IDF[d] = tfidf_

    return TF_IDF


if __name__ == '__main__':
    cultures = ['chinese.txt',
                'thai.txt',
                'japanese.txt']

    res = culture_tf_idf(cultures)
    nice_print2Ddict(res)