def calculate_wallet_size(sizes):
    flattened_sizes = sum(sizes, [])
    max_width = max(min(size) for size in sizes)
    return max_width * max(flattened_sizes)

test=[60, 50], [30, 70], [60, 30], [80, 40]
print(calculate_wallet_size([[60, 50], [30, 70], [60, 30], [80, 40]]))