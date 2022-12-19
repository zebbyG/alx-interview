def pascal_triangle(n):
    """
    A function that returns a list of lists of integer representing the Pascal’s triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle

    for z in range(0, n):
        """
        A loop to create a list after every iteration in the range
        """
        if z == 0:
            triangle.append([1])
        else:
            row = [1]
            for e in range(z - 1):
                row.append(triangle[z - 1][e] + triangle[z - 1][e + 1])
            row.append(1)
            triangle.append(row)

    return triangle
