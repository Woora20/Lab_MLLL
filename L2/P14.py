def laplace_smooth(counting, alpha):
    total_counts = sum(counting)
    num_object_types = len(counting)
    
    probabilities = [(count + alpha) / (total_counts + alpha * num_object_types) for count in counting]
    return probabilities

if __name__ == "__main__":
    counting = [0, 8, 20, 4, 12]
    smoothing_factor = 0.1
    res = laplace_smooth(counting, smoothing_factor)
    print(res)
