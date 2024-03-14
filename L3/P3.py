
def clean_txt(m):
    m = m.replace('.', ' ')
    m = m.replace(';', ' ')
    m = m.replace('\n', ' ')
    m = m.replace('  ', ' ')

    return m


def word_freq(mg):

    cleaned_text = clean_txt(mg)

    word_count = {}
    words = cleaned_text.split()

    for i in words:
        if '' or 'a' in word_count:
            pass
        elif i not in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1
      

    return word_count

if __name__ == '__main__':
    txt = "Evil is done by oneself; " + \
          "by oneself is one defiled. \n " + \
          "Evil is left undone by oneself; " + \
          "by oneself is one cleansed. \n " + \
          "Purity and impurity are one's own doing. \n" + \
          "No one purifies another. \n" + \
          "No other purifies one."
          # excerpt from Attavagga: Self, www.accesstoinsight.org

    print(txt)

    wf = word_freq(txt)
    print('\nCount:')
    print(wf)