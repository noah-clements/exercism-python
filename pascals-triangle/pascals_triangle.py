def rows(row_count):
    if row_count < 0: raise ValueError("number of rows is negative")
    if row_count == 0: return []
    triangle = []
    compute_row(row_count, triangle)
    return triangle


def compute_row(row_number, triangle):
    if row_number == 1: 
        triangle.append([1])
        return [1]
    prev_row = compute_row(row_number - 1, triangle)
    new_row = []
    for i in range(row_number):
        if i == 0 or i == row_number - 1:
            new_row.append(1)
        else:
            new_row.append(prev_row[i-1] + prev_row[i])
    triangle.append(new_row)
    return new_row

