def collect_data():
    observations = []
    counts = []

    while True:
        observation = input("Observation:")
        if observation.lower() == '':
            break

        count = int(input("Found:"))

        observations.append(observation)
        counts.append(count)

    return observations, counts

if __name__ == "__main__":
    observ, counting = collect_data()
    print("Observation:")
    print(observ)
    print(counting)
