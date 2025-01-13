"""
A simple Pascal's triangle implementation.
"""


def triangle_row(n: int) -> list[int]:
    if n == 0:
        return [1]
    
    previous_row = triangle_row(n - 1)
    row = [1]
    for col in range(1, n):
        row.append(previous_row[col - 1] + previous_row[col] + 1)
    row.append(1)

    return row
