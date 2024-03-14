def est_prob(counting):
    total_counts = sum(counting)
    probabilities = [count / total_counts for count in counting]
    return probabilities

if __name__ == "__main__":
    counting = [0, 8, 20, 4, 12]
    res = est_prob(counting)
    print(res)
