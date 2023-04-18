def maximum_value(maximum_weight, items):
    n = len(items)
    print(n)
    table = [[0 for _ in range(maximum_weight + 1)] for _ in range(n + 1)]
    print(len(table))
    print(len(table[0]))

    for i in range(1, n+1):
        for w in range(1, maximum_weight+1):
            if items[i-1]['weight'] > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w], 
                                  table[i - 1][w - items[i-1]['weight']] 
                                  + items[i-1]['value'])
    return table[n][maximum_weight]
