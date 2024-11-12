def nextFit(items, capacity):
    bins = []
    bin_capacity = capacity

    for item in items:
        if item <= bin_capacity:
            bin_capacity -= item
        else:
            bins.append(bin_capacity)
            bin_capacity = capacity - item

    bins.append(bin_capacity)
    return len(bins)

def main():
    items = [4, 8, 1, 4, 2, 1]
    capacity = 10
    num_bins = nextFit(items, capacity)
    print("Número total de contenedores utilizados:", num_bins)

if __name__ == "__main__":
    main()
